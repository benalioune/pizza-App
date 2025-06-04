import React from "react";
import styles from "./Checkout.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Checkout = () => {
    // TODO: gérer envoi POST /restau/commandes
    return (
        <div className={styles.checkout}>
            <Header />
            <main>
                <h2>Validation de la commande</h2>
                <form className={styles.form}>
                    {/* Champs livraison, paiement */}
                    <button type="submit">Confirmer la commande</button>
                </form>
            </main>
            <Footer />
        </div>
    );
};
export default Checkout;
