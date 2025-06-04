import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import styles from "./EditPizza.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const EditPizza = () => {
    const { id } = useParams();
    const [pizza, setPizza] = useState(null);

    useEffect(() => {
        fetch(`/api/restau/pizzas/${id}`)
            .then(res => res.json())
            .then(setPizza);
    }, [id]);

    const handleSubmit = e => {
        e.preventDefault();
        // PATCH /restau/pizzas/:id
    };

    if (!pizza) return <div>Chargement...</div>;
    return (
        <div className={styles.editPizza}>
            <Header admin />
            <main>
                <h2>Modifier la pizza</h2>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <label>Nom</label>
                    <input value={pizza.nom} onChange={e => setPizza({...pizza, nom: e.target.value})} required />
                    <label>Ingrédients</label>
                    <input value={pizza.ingredients} onChange={e => setPizza({...pizza, ingredients: e.target.value})} required />
                    <label>Prix (€)</label>
                    <input type="number" value={pizza.prix} onChange={e => setPizza({...pizza, prix: e.target.value})} required />
                    <button type="submit">Mettre à jour</button>
                </form>
            </main>
            <Footer />
        </div>
    );
};
export default EditPizza;
