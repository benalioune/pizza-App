import React, { useState } from "react";
import styles from "./Login.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        setLoading(true);

        try {
            const formData = new FormData();
            formData.append('username', email);
            formData.append('password', password);

            const response = await fetch("http://localhost:8000/auth/login", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error('Invalid credentials');
            }

            const data = await response.json();
            localStorage.setItem('token', data.access_token);
            window.location.href = '/menu';
        } catch (err) {
            setError(err.message || 'An error occurred during login');
            console.error('Login error:', err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className={styles.login}>
            <Header />
            <main>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <h2>Connexion</h2>
                    {error && <div className={styles.error}>{error}</div>}
                    <label>Email</label>
                    <input 
                        type="email" 
                        value={email} 
                        onChange={e => setEmail(e.target.value)} 
                        required 
                        disabled={loading}
                    />
                    <label>Mot de passe</label>
                    <input 
                        type="password" 
                        value={password} 
                        onChange={e => setPassword(e.target.value)} 
                        required 
                        disabled={loading}
                    />
                    <button type="submit" disabled={loading}>
                        {loading ? 'Connexion en cours...' : 'Se connecter'}
                    </button>
                </form>
            </main>
            <Footer />
        </div>
    );
};

export default Login;
