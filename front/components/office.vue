<script setup>
const props = defineProps({
  office: Object
})
</script>

<template>
  <div class="class1">
    <div class="class2">
      <p class="class3">{{ props.office.title }}</p>
      <p class="class4">{{ props.office.address }}</p>
      <div class="class5">
        <p>Контакты:</p>
        <template v-for="phone in props.office.phones">
          <p>{{ phone }}</p>
        </template>
      </div>
      <div class="class6">
        <p>Режим работы:</p>
        <p>{{ props.office.working_time }}</p>
      </div>
    </div>
    <div class="class7">
      <img class="class8" :src="props.office.image" alt="">
    </div>
  </div>

</template>


<style>
.class1 {
  display: flex;
  flex-direction: row;
  width: max-content;
  gap: 0.75rem;
}
.class2 {
  display: flex;
  flex-direction: column;
  width: 24rem;
}
.class3 {
  font-size: 1.5rem;
  line-height: 2rem;
  color: var(--p-surface-950);
  text-transform: uppercase;
}
.class4 {
  
}
.class5 {
  margin-top: 0.75rem;
}
.class6 {
  display: flex;
  flex-direction: row;
  gap:1.25rem;
  margin-top: 0.75rem;
}
.class7 {
  min-height: 0;
  height: 100%;
}
.class8 {
  min-height: 0;
  height: 8rem;
}

</style>