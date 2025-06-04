import { useState, useEffect } from "react";
import { getPizzas }           from "../../services/api.js";
import { useShop }             from "../../contexts/ShopContext.jsx";
import styles                  from "./Pizzas.module.scss";

export default function Pizzas() {
    const { addToCart } = useShop();
    const [pizzas, setPizzas] = useState(null);
    const [err,    setErr]    = useState(null);

    useEffect(() => {
        getPizzas()
            .then(setPizzas)
            .catch(e => setErr(e.message));
    }, []);

    if (err)             return <p className={styles.center}>Erreur : {err}</p>;
    if (pizzas === null) return <p className={styles.center}>Chargement…</p>;

    return (
        <section className={styles.wrapper}>
            <h1>Nos pizzas</h1>

            <ul className={styles.grid}>
                {pizzas.map(p => (
                    <li key={p.id}>
                        <h3>{p.name}</h3>
                        <span>{p.price.toFixed(2)} €</span>
                        <button onClick={() => addToCart(p)}>Ajouter</button>
                    </li>
                ))}
            </ul>
        </section>
    );
}
