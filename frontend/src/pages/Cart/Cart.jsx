import React from "react";
import styles from "./Cart.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Cart = () => {
    // TODO: Récupérer le panier depuis context/store
    const cart = [];
    const total = cart.reduce((sum, item) => sum + item.prix * item.qty, 0);

    return (
        <div className={styles.cart}>
            <Header />
            <main>
                <h2>Mon panier</h2>
                {cart.length === 0 ? (
                    <p>Votre panier est vide.</p>
                ) : (
                    <>
                        <ul>
                            {cart.map(item => (
                                <li key={item.id}>
                                    {item.nom} x {item.qty} — {item.prix} € / unité
                                </li>
                            ))}
                        </ul>
                        <div className={styles.total}>Total : {total} €</div>
                        <a href="/checkout" className={styles.cta}>Commander</a>
                    </>
                )}
            </main>
            <Footer />
        </div>
    );
};
export default Cart;
