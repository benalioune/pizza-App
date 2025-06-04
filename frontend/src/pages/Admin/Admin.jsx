import { NavLink, Routes, Route } from 'react-router-dom';
import AdminPizzas from './Pizzas/Pizzas.jsx';
import Orders      from './Orders/Orders.jsx';
import Users       from './Users/Users.jsx';
import styles      from './Admin.module.scss';

export default function Admin() {
    return (
        <section className={styles.admin}>
            <h1>Tableau de bord</h1>

            <nav className={styles.tabs}>
                <NavLink to="pizzas">Pizzas</NavLink>
                <NavLink to="orders">Commandes</NavLink>
                <NavLink to="users">Utilisateurs</NavLink>
            </nav>

            <Routes>
                <Route index        element={<p>Sélectionnez un onglet.</p>} />
                <Route path="pizzas" element={<AdminPizzas />} />
                <Route path="orders" element={<Orders />} />
                <Route path="users"  element={<Users />} />
            </Routes>
        </section>
    );
}
