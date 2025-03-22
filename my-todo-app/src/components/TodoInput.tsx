import React, { useState } from "react";
import "./TodoInput.css"; // Стили

type Props = {
  onAdd: (task: string) => void;
};

const TodoInput: React.FC<Props> = ({ onAdd }) => {
  const [task, setTask] = useState("");

  const handleAdd = () => {
    if (!task.trim()) return;
    onAdd(task);
    setTask("");
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleAdd();
    }
  };

  return (
    <div className="todo-input">
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        onKeyDown={handleKeyPress}
        placeholder="Добавить новую задачу..."
      />
      <button onClick={handleAdd}>➕</button>
    </div>
  );
};

export default TodoInput;
