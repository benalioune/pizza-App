import { useEffect, useState } from 'react';
import { getOrders } from '../../../services/api.js';      // 2 niveaux
import styles from './Orders.module.scss';

export default function Orders() {
    const [orders, setOrders] = useState(null);
    useEffect(() => { getOrders().then(setOrders); }, []);

    if (!orders) return <p>Chargement…</p>;

    return (
        <div className={styles.orders}>
            <h2>Commandes</h2>

            {orders.length === 0 ? (
                <p>Aucune commande.</p>
            ) : (
                <table>
                    <thead>
                    <tr><th>ID</th><th>Nb pizzas</th><th>Total €</th></tr>
                    </thead>
                    <tbody>
                    {orders.map(o => (
                        <tr key={o.id}>
                            <td>#{o.id}</td>
                            <td>{o.items.length}</td>
                            <td>{o.total.toFixed(2)}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}
