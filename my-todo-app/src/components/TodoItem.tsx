import React from "react";
import "./TodoItem.css"; // Добавим стили

type Props = {
  task: string;
  onDelete: () => void;
};

const TodoItem: React.FC<Props> = ({ task, onDelete }) => {
  return (
    <li className="todo-item">
      <span>{task}</span>
      <button className="delete-btn" onClick={onDelete}>✖</button>
    </li>
  );
};

export default TodoItem;
