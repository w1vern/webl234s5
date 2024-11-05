<script setup>
import Toast from 'primevue/toast';
const authStore = useAuthStore()
onBeforeMount(async () => {
  await authStore.fetch_session()
})
</script>

<template>
  <div class="all">
    <Toast  position="bottom-right"/>
    <div class="main">
      <NuxtLoadingIndicator />
      <NuxtPage />
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
}

.main {
  background-color: var(--p-surface-300);
  height: max-content;
}
</style>