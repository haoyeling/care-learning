async function getTasks() {
  const r = await fetch("http://127.0.0.1:8000/tasks");
  const data = await r.json();
  const titles = data.filter(t => t.done === false).map(t => t.title)
  console.log(titles);
}

getTasks();