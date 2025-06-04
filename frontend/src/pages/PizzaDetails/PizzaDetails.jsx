import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import styles from "./PizzaDetails.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const PizzaDetails = () => {
    const { id } = useParams();
    const [pizza, setPizza] = useState(null);

    useEffect(() => {
        fetch(`localhost:8000/restau/menu`)
            .then(res => res.json())
            .then(setPizza);
    }, [id]);

    if (!pizza) return <div>Chargement...</div>;

    return (
        <div className={styles.details}>
            <Header />
            <main>
                <div className={styles.card}>
                    <h2>{pizza.nom}</h2>
                    <p><b>Ingrédients :</b> {pizza.ingredients}</p>
                    <p><b>Prix :</b> {pizza.prix} €</p>
                    <button>Ajouter au panier</button>
                </div>
            </main>
            <Footer />
        </div>
    );
};
export default PizzaDetails;
