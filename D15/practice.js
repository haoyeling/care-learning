const tasks = [
  { task_id: 1, title: "买菜", done: false },
  { task_id: 2, title: "做饭", done: true },
  { task_id: 3, title: "写代码", done: false }
];

const pending = tasks.filter(t => t.done === false);
console.log(pending);

const titles = tasks.map(t => t.title);
console.log(titles);

const found = tasks.find(t => t.task_id === 2);
console.log(found)

const pendings = tasks.filter(t => t.done === true);
console.log(pendings);

const ids = tasks.map(t => t.task_id);
console.log(ids);

const founds = tasks.find(t => t.title === '写代码');
console.log(founds);