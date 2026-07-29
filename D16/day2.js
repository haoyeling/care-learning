const name = "买菜";
const done =false;

console.log(`任务: ${name}, 完成: ${done}`);

const tasks = [
  { task_id: 1, title: "买菜", done: false },
  { task_id: 2, title: "做饭", done: true },
  { task_id: 3, title: "写代码", done: false }
];

function format({task_id, title, done}){
    const mark = done ? "√" : " "
    return `[${task_id}] ${mark} ${title}`
}
tasks.forEach(t => console.log(format(t)))

function summary({title, done}){
    const status = done ? "已完成" : "还没做"
    return `${title} ${status}`
}
tasks.forEach(t => console.log(summary(t)))