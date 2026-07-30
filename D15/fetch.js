async function getTasks() {
  const r = await fetch("http://127.0.0.1:8000/tasks");
  const data = await r.json();
  const titles = data.filter(t => t.done === false).map(t => t.title)
  console.log(titles);
}

getTasks();

//async 标在函数上,意思是"这个函数里面可能有暂停"
//await 标在具体那一行,意思是"这行要等,等到了再往下"
//用于处理异步