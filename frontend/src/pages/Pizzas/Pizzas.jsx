import React, { useEffect, useState } from "react";
import styles from "./Pizzas.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Pizzas = () => {
    const [pizzas, setPizzas] = useState([]);
    useEffect(() => {
        fetch("localhost:8000/restau/menu", {method: "POST", body: JSON.stringify(setPizzas)})
            .then(res => res.json())
            .then(setPizzas);
    }, []);
    return (
        <div className={styles.pizzas}>
            <Header />
            <main>
                <h2>Nos Pizzas</h2>
                <div className={styles.grid}>
                    {pizzas.map(pizza => (
                        <div key={pizza.id} className={styles.card}>
                            <h3>{pizza.nom}</h3>
                            <p>{pizza.ingredients}</p>
                            <div className={styles.price}>{pizza.prix} €</div>
                            <a href={`/pizzas/${pizza.id}`} className={styles.details}>Voir détail</a>
                            <button>Ajouter au panier</button>
                        </div>
                    ))}
                </div>
            </main>
            <Footer />
        </div>
    );
};
export default Pizzas;
