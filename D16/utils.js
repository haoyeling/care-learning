export function format({ task_id, title, done }) {
    const mark = done ? "√" : " ";
    return `[${task_id}] ${mark} ${title}`;
}

export function summary({ title, done }) {
    const status = done ? "已完成" : "还没做";
    return `${title} ${status}`;
}