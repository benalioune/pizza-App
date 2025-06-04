import React from "react";
import styles from "./About.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const About = () => (
    <div className={styles.about}>
        <Header />
        <main>
            <h2>À propos</h2>
            <p>PizzaTech, la tech au service du goût. Créée par passion, pour les vrais gourmands !</p>
        </main>
        <Footer />
    </div>
);
export default About;
