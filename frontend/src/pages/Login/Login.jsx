import React, { useState } from "react";
import styles from "./Login.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const handleSubmit = e => {
        e.preventDefault();
        useEffect(() => {
        fetch("localhost:8000/login", {method: "POST", body: JSON.stringify(setEmail, setPassword)})
            .then(res => res.json());
            
    }, []);
    };

    return (
        <div className={styles.login}>
            <Header />
            <main>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <h2>Connexion</h2>
                    <label>Email</label>
                    <input type="email" value={email} onChange={e=>setEmail(e.target.value)} required />
                    <label>Mot de passe</label>
                    <input type="password" value={password} onChange={e=>setPassword(e.target.value)} required />
                    <button type="submit">Se connecter</button>
                </form>
            </main>
            <Footer />
        </div>
    );
};
export default Login;
