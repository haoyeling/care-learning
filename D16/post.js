async function createTask(title) {
    const r = await fetch("http://127.0.0.1:8000/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: title })
    });
    const data = await r.json();
    console.log(data);
}

createTask("从 JS 创建的任务");