import React from "react";
import styles from "./NotFound.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const NotFound = () => (
    <div className={styles.notfound}>
        <Header />
        <main>
            <h2>404 — Page non trouvée</h2>
            <a href="/">Retour à l'accueil</a>
        </main>
        <Footer />
    </div>
);
export default NotFound;
