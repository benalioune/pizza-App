import { useEffect, useState } from "react";
import {
    getPizzas,
    addPizza,
    updatePizza,
    deletePizza,
} from "../../../services/api.js";   // ← 3 niveaux
import styles from "./Pizzas.module.scss";

export default function AdminPizzas() {
    const [list, setList]     = useState(null);
    const [form, setForm]     = useState({ name: "", price: "" });
    const [editId, setEditId] = useState(null);
    const [error,  setError]  = useState(null);

    /* ------- sync serveur ------- */
    const refresh = () =>
        getPizzas()
            .then(setList)
            .catch(e => setError(e.message));

    useEffect(() => { refresh(); }, []);

    /* ------- handlers ------- */
    const handleChange = e =>
        setForm({ ...form, [e.target.name]: e.target.value });

    const reset = () => setForm({ name: "", price: "" });

    const submit = async e => {
        e.preventDefault();
        if (!form.name || !form.price) return;

        try {
            editId
                ? await updatePizza(editId, form.name, +form.price)
                : await addPizza(form.name, +form.price);
            setEditId(null);
            reset();
            refresh();
        } catch (err) {
            setError(err.message);
        }
    };

    const startEdit = p => {
        setForm({ name: p.name, price: p.price });
        setEditId(p.id);
    };

    /* ------- render ------- */
    if (error) return <p style={{ color: "red" }}>Erreur : {error}</p>;
    if (!list) return <p>Chargement…</p>;

    return (
        <div className={styles.wrapper}>
            <h2>Gestion des pizzas</h2>

            <form className={styles.form} onSubmit={submit}>
                <input
                    name="name"
                    placeholder="Nom"
                    value={form.name}
                    onChange={handleChange}
                />
                <input
                    name="price"
                    placeholder="Prix"
                    type="number"
                    step="0.1"
                    value={form.price}
                    onChange={handleChange}
                />
                <button>{editId ? "MAJ" : "Ajouter"}</button>
            </form>

            <table>
                <thead>
                <tr><th>Nom</th><th>Prix €</th><th></th></tr>
                </thead>
                <tbody>
                {list.map(p => (
                    <tr key={p.id}>
                        <td>{p.name}</td>
                        <td>{p.price.toFixed(2)}</td>
                        <td>
                            <button onClick={() => startEdit(p)}>✏️</button>
                            <button onClick={() => deletePizza(p.id).then(refresh)}>🗑️</button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}
