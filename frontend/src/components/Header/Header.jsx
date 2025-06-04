import React from "react";
import styles from "./Header.module.scss";

const Header = ({ admin }) => (
    <header className={styles.header}>
        <div className={styles.logo}>
            <a href="/">🍕 PizzaTech</a>
        </div>
        <nav>
            {admin ? (
                <>
                    <a href="/admin/pizzas">Pizzas</a>
                    <a href="/admin/orders">Commandes</a>
                    <a href="/admin/users">Utilisateurs</a>
                    <a href="/admin/todos">Tâches</a>
                    <a href="/">Quitter l’admin</a>
                </>
            ) : (
                <>
                    <a href="/pizzas">Nos Pizzas</a>
                    <a href="/cart">Panier</a>
                    <a href="/orders">Commandes</a>
                    <a href="/profile">Profil</a>
                    <a href="/login">Connexion</a>
                </>
            )}
        </nav>
    </header>
);

export default Header;
