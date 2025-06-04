import React, { useEffect, useState } from "react";
import styles from "./PizzasAdmin.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const PizzasAdmin = () => {
    const [pizzas, setPizzas] = useState([]);
    useEffect(() => {
        fetch("/api/restau/pizzas").then(res => res.json()).then(setPizzas);
    }, []);
    return (
        <div className={styles.pizzasAdmin}>
            <Header admin />
            <main>
                <h2>Admin — Gestion des pizzas</h2>
                <a href="/admin/pizzas/add" className={styles.addBtn}>Ajouter une pizza</a>
                <ul>
                    {pizzas.map(pz => (
                        <li key={pz.id}>
                            <b>{pz.nom}</b> — {pz.prix}€
                            <a href={`/admin/pizzas/${pz.id}/edit`}>Éditer</a>
                        </li>
                    ))}
                </ul>
            </main>
            <Footer />
        </div>
    );
};
export default PizzasAdmin;
