import React from "react";
import styles from "./Footer.module.scss";

const Footer = () => (
    <footer className={styles.footer}>
        <p>
            &copy; {new Date().getFullYear()} PizzaTech — Projet pédagogique React + Python. <br />
            Design inspiré Domino's 🍕 | <a href="/about">À propos</a> | <a href="/contact">Contact</a>
        </p>
    </footer>
);

export default Footer;
