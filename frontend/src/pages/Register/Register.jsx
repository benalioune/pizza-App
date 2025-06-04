import React, { useState } from "react";
import styles from "./Register.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const handleSubmit = e => {
        e.preventDefault();
        useEffect(() => {
                fetch("localhost:8000/signup", {method: "POST", body:JSON.stringify(setEmail, setPassword)})
                    .then(res => res.json())
                    .then(data);
        })
    };

    return (
        <div className={styles.register}>
            <Header />
            <main>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <h2>Inscription</h2>
                    <label>Email</label>
                    <input type="email" value={email} onChange={e=>setEmail(e.target.value)} required />
                    <label>Mot de passe</label>
                    <input type="password" value={password} onChange={e=>setPassword(e.target.value)} required />
                    <button type="submit">S'inscrire</button>
                </form>
            </main>
            <Footer />
        </div>
    );
};
export default Register;
