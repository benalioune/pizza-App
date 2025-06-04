import { NavLink } from 'react-router-dom';
import styles from './Header.module.scss';

export default function Header() {
    return (
        <header className={styles.header}>
            <h1 className={styles.brand}>PizzaTech</h1>
            <nav className={styles.nav}>
                <NavLink to="/"       end>Accueil</NavLink>
                <NavLink to="/pizzas">Pizzas</NavLink>
                <NavLink to="/cart">Panier</NavLink>
                <NavLink to="/admin">Admin</NavLink>
            </nav>
        </header>
    );
}
