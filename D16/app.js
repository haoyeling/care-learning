import {format, summary} from "./utils.js"

const tasks = [
    { task_id: 1, title: "买菜", done: false },
    { task_id: 2, title: "做饭", done: true }
];

tasks.forEach(t => console.log(format(t)));