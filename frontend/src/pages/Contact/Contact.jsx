import React from "react";
import styles from "./Contact.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Contact = () => (
    <div className={styles.contact}>
        <Header />
        <main>
            <h2>Contact</h2>
            <form className={styles.form}>
                <label>Votre email</label>
                <input type="email" />
                <label>Votre message</label>
                <textarea rows={4} />
                <button type="submit">Envoyer</button>
            </form>
        </main>
        <Footer />
    </div>
);
export default Contact;
