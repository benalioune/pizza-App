import React from "react";
import styles from "./Home.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Home = () => (
    <div className={styles.home}>
        <Header />
        <main>
            <section className={styles.hero}>
                <h1>Bienvenue chez PizzaTech</h1>
                <p>Commandez vos pizzas préférées en ligne et gérez vos commandes en toute simplicité.</p>
                <a className={styles.cta} href="/pizzas">Voir nos pizzas</a>
            </section>
        </main>
        <Footer />
    </div>
);

export default Home;
