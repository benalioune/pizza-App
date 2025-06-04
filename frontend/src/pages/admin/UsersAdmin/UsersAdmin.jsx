import React, { useEffect, useState } from "react";
import styles from "./UsersAdmin.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const UsersAdmin = () => {
    const [users, setUsers] = useState([]);
    useEffect(() => {
        fetch("/api/users").then(res=>res.json()).then(setUsers); // adapter l’endpoint si besoin
    }, []);
    return (
        <div className={styles.usersAdmin}>
            <Header admin />
            <main>
                <h2>Admin — Utilisateurs</h2>
                <ul>
                    {users.map(user => (
                        <li key={user.id}>
                            {user.email} — {user.role}
                        </li>
                    ))}
                </ul>
            </main>
            <Footer />
        </div>
    );
};
export default UsersAdmin;
