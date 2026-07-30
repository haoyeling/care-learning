<script setup>
defineProps({
  task: Object
})

defineEmits(['done', 'remove'])
</script>

<template>
  <li class="item" :class="{ finished: task.done }">
    <span class="title">{{ task.title }}</span>
    <div class="actions">
      <button v-if="!task.done" @click="$emit('done', task.task_id)">完成</button>
      <button class="danger" @click="$emit('remove', task.task_id)">删除</button>
    </div>
  </li>
</template>

<style scoped>
.item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid #2a2a2a;
}
.item.finished .title {
  text-decoration: line-through;
  opacity: 0.4;
}
.title { flex: 1; }
.actions { display: flex; gap: 8px; }
button {
  padding: 4px 12px;
  font-size: 13px;
  border: 1px solid #3a3a3a;
  background: transparent;
  color: inherit;
  border-radius: 4px;
  cursor: pointer;
}
button:hover { background: #2a2a2a; }
button.danger:hover { background: #5a2020; }
</style>