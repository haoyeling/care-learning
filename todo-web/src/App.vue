<script setup>
import { ref, onMounted } from 'vue'

const tasks = ref([])
//ref函数立刻变成响应式

async function loadTasks() {
  const r = await fetch("http://127.0.0.1:8000/tasks")
  tasks.value = await r.json()
  //有ref就要用.value
}

onMounted(loadTasks)
//组件挂到页面后，执行这个函数

const newTitle = ref("")

async function addTask() {
  if (!newTitle.value.trim()) return      // 空标题不提交

  await fetch("http://127.0.0.1:8000/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: newTitle.value })
  })

  newTitle.value = ""      // 清空输入框
  await loadTasks()        // 重新拉一次列表
}
//增加条目

async function markDone(id) {
  await fetch(`http://127.0.0.1:8000/tasks/${id}/done`, { method: "PUT" })
  await loadTasks()
}

async function removeTask(id) {
  await fetch(`http://127.0.0.1:8000/tasks/${id}`, { method: "DELETE" })
  await loadTasks()
}


</script>

<template>
  <h1>
    我的任务
    <input v-model="newTitle" placeholder="输入新任务" />
    <button @click="addTask">添加</button>
  </h1>
  <ul>
    <li v-for="t in tasks" :key="t.task_id">
      {{ t.title }} - {{ t.done ? "已完成" : "还没做" }}
      <button @click="markDone(t.task_id)">完成</button>
      <button @click="removeTask(t.task_id)">删除</button>
</li>
  </ul>
</template>
