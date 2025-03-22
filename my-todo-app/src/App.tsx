import React from "react";
import TodoList from "./components/TodoList";
import "./App.css";

const App: React.FC = () => {
  const today = new Date().toLocaleDateString("ru-RU", {
    weekday: "long",
    day: "numeric",
    month: "long",
  });

  return (
    <div className="app">
      <header>
        <h1>✅ Мой список дел</h1>
        <p>{today}</p>
      </header>
      <TodoList />
    </div>
  );
};

export default App;
