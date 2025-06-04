import React, { useEffect, useState } from "react";
import styles from "./TodosAdmin.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const TodosAdmin = () => {
    const [todos, setTodos] = useState([]);
    useEffect(() => {
        fetch("/api/todos").then(res=>res.json()).then(setTodos); // adapter l’endpoint
    }, []);
    return (
        <div className={styles.todosAdmin}>
            <Header admin />
            <main>
                <h2>Admin — Tâches</h2>
                <ul>
                    {todos.map(todo => (
                        <li key={todo.id}>
                            <b>{todo.title}</b> — {todo.status}
                        </li>
                    ))}
                </ul>
            </main>
            <Footer />
        </div>
    );
};
export default TodosAdmin;
