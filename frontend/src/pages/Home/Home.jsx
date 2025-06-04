import { Link } from "react-router-dom";
import styles    from "./Home.module.scss";

export default function Home() {
    return (
        <>
            {/* HÉRO */}
            <section className={styles.hero}>
                <div className={styles.content}>
                    <h1>Livraison de pizzas <span>100 % plaisir</span></h1>
                    <p>Pâte maison, ingrédients premium, service éclair.<br />
                        Essayez la différence !</p>
                    <Link to="/pizzas" className={styles.cta}>Voir le menu</Link>
                </div>
            </section>

            {/* POURQUOI NOUS ? */}
            <section className={styles.features}>
                <h2>Pourquoi choisir PizzaTech&nbsp;?</h2>
                <ul>
                    <li>
                        <img src="https://cdn-icons-png.flaticon.com/512/3595/3595455.png" alt="" />
                        <h3>Qualité</h3>
                        <p>Produits frais livrés chaque matin, cuisson sur pierre.</p>
                    </li>
                    <li>
                        <img src="https://cdn-icons-png.flaticon.com/512/1046/1046784.png" alt="" />
                        <h3>Rapidité</h3>
                        <p>Moins de 30 min entre votre clic et la première bouchée.</p>
                    </li>
                    <li>
                        <img src="https://cdn-icons-png.flaticon.com/512/992/992700.png" alt="" />
                        <h3>Programmez&nbsp;!</h3>
                        <p>Commandez maintenant — choisissez l’heure qui vous arrange.</p>
                    </li>
                </ul>
                <Link to="/pizzas" className={styles.altCta}>Je me laisse tenter 🍕</Link>
            </section>
        </>
    );
}
