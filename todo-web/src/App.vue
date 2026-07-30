<script setup>
import { ref, onMounted } from 'vue'
import TaskItem from './components/TaskItem.vue'

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
  <h1>我的任务</h1>

    <div class="add-box">
       <input v-model="newTitle" placeholder="输入新任务" />
       <button @click="addTask">添加</button>
    </div>

  <ul>
    <TaskItem
      v-for="t in tasks"
      :key="t.task_id"
      :task="t"
      @done="markDone"
      @remove="removeTask"
    />
  </ul>
</template>

<style scoped>
h1 {
  font-size: 28px;
  font-weight: 600;
  text-align: left;
  margin: 0 0 24px;
}

.add-box {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.add-box input {
  flex: 1;
  padding: 10px 14px;
  background: #1a1a1a;
  border: 1px solid #333;
  border-radius: 6px;
  color: inherit;
  font-size: 14px;
}

.add-box input:focus {
  outline: none;
  border-color: #666;
}

.add-box button {
  padding: 10px 20px;
  background: #2d5a3d;
  border: none;
  border-radius: 6px;
  color: #e8e8e8;
  cursor: pointer;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
  border-top: 1px solid #2a2a2a;
}
</style>
