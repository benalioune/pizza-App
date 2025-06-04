import { useEffect, useState } from "react";
import {
    getUsers,
    addUser,
    updateUser,
    deleteUser,
} from "../../../services/api.js";   // ← 3 niveaux
import styles from "./Users.module.scss";

export default function Users() {
    const [list, setList]     = useState(null);
    const [form, setForm]     = useState({ name: "", email: "" });
    const [editId, setEditId] = useState(null);
    const [error,  setError]  = useState(null);

    const refresh = () =>
        getUsers()
            .then(setList)
            .catch(e => setError(e.message));

    useEffect(() => { refresh(); }, []);

    const handleChange = e =>
        setForm({ ...form, [e.target.name]: e.target.value });

    const reset = () => setForm({ name: "", email: "" });

    const submit = async e => {
        e.preventDefault();
        if (!form.name || !form.email) return;

        try {
            editId
                ? await updateUser(editId, form.name, form.email)
                : await addUser(form.name, form.email);
            setEditId(null);
            reset();
            refresh();
        } catch (err) {
            setError(err.message);
        }
    };

    const startEdit = u => {
        setForm({ name: u.name, email: u.email });
        setEditId(u.id);
    };

    /* ------- render ------- */
    if (error) return <p style={{ color: "red" }}>Erreur : {error}</p>;
    if (!list)  return <p>Chargement…</p>;

    return (
        <div className={styles.wrapper}>
            <h2>Gestion des utilisateurs</h2>

            <form className={styles.form} onSubmit={submit}>
                <input
                    name="name"
                    placeholder="Nom"
                    value={form.name}
                    onChange={handleChange}
                />
                <input
                    name="email"
                    placeholder="Email"
                    value={form.email}
                    onChange={handleChange}
                />
                <button>{editId ? "MAJ" : "Ajouter"}</button>
            </form>

            <table>
                <thead>
                <tr><th>Nom</th><th>Email</th><th></th></tr>
                </thead>
                <tbody>
                {list.map(u => (
                    <tr key={u.id}>
                        <td>{u.name}</td>
                        <td>{u.email}</td>
                        <td>
                            <button onClick={() => startEdit(u)}>✏️</button>
                            <button onClick={() => deleteUser(u.id).then(refresh)}>🗑️</button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}
