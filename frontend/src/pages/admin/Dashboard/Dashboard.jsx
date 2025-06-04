import React from "react";
import styles from "./Dashboard.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const Dashboard = () => (
    <div className={styles.dashboard}>
        <Header admin />
        <main>
            <h2>Admin - Dashboard</h2>
            <ul>
                <li><a href="/admin/pizzas">Gérer les pizzas</a></li>
                <li><a href="/admin/orders">Gérer les commandes</a></li>
                <li><a href="/admin/users">Gérer les utilisateurs</a></li>
                <li><a href="/admin/todos">Tâches de l’équipe</a></li>
            </ul>
        </main>
        <Footer />
    </div>
);
export default Dashboard;
