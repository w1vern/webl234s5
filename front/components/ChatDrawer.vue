<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'

const open = ref(false)
const chats = ref([])
const activeChatId = ref(null)
const messages = ref([])
const newMessage = ref('')
const ws = ref(null)
const wsConnected = ref(false)
const loadingChats = ref(false)
const loadingMessages = ref(false)
const creatingChat = ref(false)
const scrollAnchor = ref(null)



function buildWsUrl(chatId) {
  const proto = window.location.protocol === 'https:' ? 'wss' : 'ws'
  let url = `ws://localhost:8000/api/chat/ws/${chatId}`

  //url += (url.includes('?') ? '&' : '?') + `t=${Date.now()}`
  return url
}


async function fetchChats() {
  loadingChats.value = true
  try {
    const { data, error, status } = await useMyFetch('/api/chat')
    if (data?.value) chats.value = data.value
    else chats.value = []
  } catch (e) {
    console.error('fetchChats', e)
    chats.value = []
  } finally {
    loadingChats.value = false
  }
}

async function createChat() {
  creatingChat.value = true
  try {
    const { data, error, status } = await useMyFetch('/api/chat', { method: 'post' })
    if (data?.value) {
      chats.value.unshift(data.value)
      selectChat(data.value)
    }
  } catch (e) {
    console.error('createChat', e)
  } finally {
    creatingChat.value = false
  }
}

async function fetchMessages(chatId) {
  loadingMessages.value = true
  try {
    const { data } = await useMyFetch(`/api/chat/${chatId}/messages`)
    messages.value = (data?.value || []).map(m => ({ text: m.text, from_user: !!m.from_user }))
    await nextTick()
    scrollToBottom()
  } catch (e) {
    console.error('fetchMessages', e)
    messages.value = []
  } finally {
    loadingMessages.value = false
  }
}


let reconnectTimer = null
let reconnectAttempts = 0

function openWs(chatId) {
  if (!chatId) return
  closeWs()

  const url = buildWsUrl(chatId)

  try {
    ws.value = new WebSocket(url)
    wsConnected.value = false

    ws.value.onopen = () => {
      wsConnected.value = true
      reconnectAttempts = 0
    }

    ws.value.onmessage = ev => {
      const text = ev.data
      messages.value.push({ text, from_user: false })
      nextTick().then(scrollToBottom)
    }

    ws.value.onclose = ev => {
      wsConnected.value = false
      if (!ev.wasClean) tryReconnect(chatId)
    }

    ws.value.onerror = err => {
      console.error('WS error', err)
      wsConnected.value = false
    }
  } catch (e) {
    console.error('openWs exception', e)
  }
}

function tryReconnect(chatId) {
  if (reconnectAttempts >= 5) return
  reconnectAttempts++
  const backoff = Math.min(1000 * (2 ** (reconnectAttempts - 1)), 5000)
  if (reconnectTimer) clearTimeout(reconnectTimer)
  reconnectTimer = setTimeout(() => {
    openWs(chatId)
  }, backoff)
}

function closeWs() {
  if (reconnectTimer) { clearTimeout(reconnectTimer); reconnectTimer = null }
  if (ws.value) {
    try { ws.value.close() } catch (e) {}
    ws.value = null
  }
  wsConnected.value = false
  reconnectAttempts = 0
}

function selectChat(chat) {
  if (!chat) return
  if (activeChatId.value === chat.id) return
  activeChatId.value = chat.id
  messages.value = []
  fetchMessages(chat.id)
  openWs(chat.id)
}

function sendMessage() {
  const text = newMessage.value && newMessage.value.trim()
  if (!text || !activeChatId.value) return

  messages.value.push({ text, from_user: true })
  nextTick().then(scrollToBottom)

  if (ws.value && ws.value.readyState === WebSocket.OPEN) {
    ws.value.send(text)
  } else {
    console.warn('WS closed — сообщение отправлено локально, но не доставлено на сервер.')
  }

  newMessage.value = ''
}

function toggle() {
  open.value = !open.value
  if (open.value && chats.value.length === 0) fetchChats()
}

function closeDrawer() {
  open.value = false
  activeChatId.value = null
  messages.value = []
  closeWs()
}

function scrollToBottom() {
  if (!scrollAnchor.value) return
  try { scrollAnchor.value.scrollIntoView({ behavior: 'smooth', block: 'end' }) } catch (e) {}
}

onBeforeUnmount(() => {
  closeWs()
})
</script>

<template>
  <div>
    <button class="chat-toggle" @click="toggle" aria-label="Open chat">💬</button>

    <transition name="fade">
      <div v-if="open" class="chat-drawer" role="dialog" aria-modal="true">
        <div class="chat-header">
          <div class="title">Чат</div>
          <div class="controls">
            <button :disabled="creatingChat" @click="createChat">Новый чат</button>
            <button class="close-btn" @click="closeDrawer">✕</button>
          </div>
        </div>

        <div class="chat-body">
          <aside class="chat-list">
            <div v-if="loadingChats" class="muted">Загрузка чатов...</div>
            <div v-else-if="chats.length === 0" class="muted">Чатов нет. Создайте новый.</div>
            <ul>
              <li v-for="c in chats" :key="c.id" :class="{ active: c.id === activeChatId }" @click="selectChat(c)">
                <div class="chat-name">{{ c.name || ('Чат ' + String(c.id).slice(0, 6)) }}</div>
              </li>
            </ul>
          </aside>

          <section class="chat-messages-area">
            <div class="chat-meta">
              <div v-if="!activeChatId" class="muted">Выберите чат слева</div>
              <div v-else>
                <strong>Чат: {{ String(activeChatId).slice(0,8) }}</strong>
                <span class="ws-status" :class="{ connected: wsConnected }">
                  {{ wsConnected ? 'online' : 'offline' }}
                </span>
              </div>
            </div>

            <div class="messages" v-if="activeChatId">
              <div v-if="loadingMessages" class="muted">Загрузка сообщений...</div>
              <div v-else>
                <div v-for="(m, idx) in messages" :key="idx" class="message" :class="{ 'from-user': m.from_user, 'from-back': !m.from_user }">
                  <div class="bubble">{{ m.text }}</div>
                </div>
                <div ref="scrollAnchor"></div>
              </div>
            </div>

            <div class="chat-input" v-if="activeChatId">
              <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Напишите сообщение..." />
              <button @click="sendMessage">Отправить</button>
            </div>
          </section>
        </div>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.chat-toggle { 
  position: fixed; 
  right: 1.25rem; 
  bottom: 1.25rem; 
  z-index: 2000; 
  width: 3.5rem; 
  height: 3.5rem; 
  border-radius: 999px; 
  border: none; 
  background: var(--p-primary-400); 
  color: white; 
  font-size: 1.25rem; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
  cursor: pointer; 
  box-shadow: 0 6px 18px rgba(0,0,0,0.12); 
}
.chat-toggle:hover {
  background: var(--p-primary-300);
}

.chat-drawer { 
  position: fixed; 
  right: 1rem; 
  bottom: 1rem; 
  top: 6rem; 
  width: 60vw; 
  max-width: 1000px; 
  z-index: 2000; 
  background: var(--p-surface-200); 
  border-radius: 8px; 
  box-shadow: 0 12px 40px rgba(0,0,0,0.2); 
  display: flex; 
  flex-direction: column; 
  overflow: hidden; 
}

.chat-header { 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  padding: 1.5rem; 
  border-bottom: 1px solid var(--p-surface-600); 
  color: var(--p-surface-950); 
  font-size: 1.5rem; 
}
.chat-header button {
  padding: 0.75rem 1rem;
  border: none;
  background: var(--p-surface-300);
  color: var(--p-surface-950);
  border-radius: 6px;
  cursor: pointer;
}
.chat-header button:hover {
  background: var(--p-surface-400);
}
.chat-header .close-btn {
  background: none;
  font-size: 1.5rem;
  padding: 0.5rem;
}
.chat-header .close-btn:hover {
  background: var(--p-surface-300);
  border-radius: 50%;
}

.chat-body { 
  display: flex; 
  flex: 1; 
  min-height: 0; 
}

.chat-list { 
  width: 240px; 
  border-right: 1px solid var(--p-surface-600); 
  padding: 0.75rem; 
  overflow-y: auto; 
  background: var(--p-surface-100); 
}
.chat-list ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.chat-list li {
  padding: 0.75rem;
  cursor: pointer;
  border-radius: 6px;
}
.chat-list li:hover {
  background: var(--p-surface-200);
}
.chat-list li.active {
  background: var(--p-surface-300);
}
.chat-list .chat-name {
  color: var(--p-surface-950);
  font-size: 1.1rem;
}

.chat-messages-area { 
  display: flex; 
  flex-direction: column; 
  flex: 1; 
  padding: 0.75rem; 
  min-width: 0; 
}

.chat-meta {
  padding: 0.75rem;
  border-bottom: 1px solid var(--p-surface-600);
  color: var(--p-surface-950);
  font-size: 1.2rem;
}

.messages { 
  flex: 1; 
  overflow-y: auto; 
  padding: 0.5rem 0; 
  display: flex; 
  flex-direction: column; 
  gap: 0.5rem; 
}

.message { 
  display: flex; 
  width: 100%; 
}

.message .bubble { 
  max-width: 70%; 
  padding: 0.6rem 0.9rem; 
  border-radius: 12px; 
  font-size: 1.1rem;
}

.message.from-user { 
  justify-content: flex-end; 
}

.message.from-user .bubble { 
  background: var(--p-primary-400); 
  color: white; 
  border-bottom-right-radius: 4px; 
}

.message.from-back { 
  justify-content: flex-start; 
}

.message.from-back .bubble { 
  background: var(--p-surface-100); 
  color: var(--p-surface-950); 
  border-bottom-left-radius: 4px; 
}

.chat-input { 
  display: flex; 
  gap: 0.5rem; 
  padding-top: 0.5rem; 
  border-top: 1px solid var(--p-surface-600); 
}

.chat-input input[type="text"] { 
  flex: 1; 
  padding: 0.6rem; 
  border-radius: 6px; 
  border: 1px solid var(--p-surface-600); 
  background: var(--p-surface-100);
  color: var(--p-surface-950);
}

.chat-input button {
  padding: 0.6rem 1rem;
  border: none;
  background: var(--p-primary-400);
  color: white;
  border-radius: 6px;
  cursor: pointer;
}
.chat-input button:hover {
  background: var(--p-primary-300);
}

.muted { 
  color: var(--p-surface-500); 
  font-size: 1.1rem;
  text-align: center;
  padding: 1rem;
}

.ws-status { 
  margin-left: 0.75rem; 
  font-size: 0.85rem; 
  padding: 0.2rem 0.45rem; 
  border-radius: 999px; 
  background: var(--p-surface-300); 
}

.ws-status.connected { 
  background: var(--p-primary-100); 
  color: var(--p-primary-400); 
}

.fade-enter-active, .fade-leave-active { 
  transition: opacity .15s; 
}

.fade-enter-from, .fade-leave-to { 
  opacity: 0; 
}
</style>