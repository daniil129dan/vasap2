import React, { useState, useEffect } from "react";
import TodoItem from "./TodoItem";
import TodoInput from "./TodoInput";
import "./TodoList.css"; // Стили

const TodoList: React.FC = () => {
  const [tasks, setTasks] = useState<string[]>([]);

  useEffect(() => {
    const savedTasks = localStorage.getItem("tasks");
    if (savedTasks) {
      setTasks(JSON.parse(savedTasks));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }, [tasks]);

  const addTask = (task: string) => {
    setTasks([...tasks, task]);
  };

  const deleteTask = (index: number) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  return (
    <div className="todo-list">
      <h2>📋 Список задач</h2>
      <TodoInput onAdd={addTask} />
      {tasks.length > 0 ? (
        <ul>
          {tasks.map((task, index) => (
            <TodoItem key={index} task={task} onDelete={() => deleteTask(index)} />
          ))}
        </ul>
      ) : (
        <p>🎉 Все задачи выполнены!</p>
      )}
    </div>
  );
};

export default TodoList;
