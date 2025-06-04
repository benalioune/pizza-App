import React, { useState } from "react";
import styles from "./AddPizza.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const AddPizza = () => {
    const [nom, setNom] = useState("");
    const [ingredients, setIngredients] = useState("");
    const [prix, setPrix] = useState("");
    const handleSubmit = e => {
        e.preventDefault();
        useEffect(() => {
                fetch("localhost:8000/restau/menu", {method: "POST", body: JSON.stringify(setNom, setIngredients, setPrix)})
                    .then(res => res.json())
                    .then(setNom, setIngredients, setPrix);
            }, []);
    };
    
    return (
        <div className={styles.addPizza}>
            <Header admin />
            <main>
                <h2>Ajouter une pizza</h2>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <label>Nom</label>
                    <input value={nom} onChange={e=>setNom(e.target.value)} required />
                    <label>Ingrédients</label>
                    <input value={ingredients} onChange={e=>setIngredients(e.target.value)} required />
                    <label>Prix (€)</label>
                    <input type="number" value={prix} onChange={e=>setPrix(e.target.value)} required />
                    <button type="submit">Créer</button>
                </form>
            </main>
            <Footer />
        </div>
    );
};
export default AddPizza;
