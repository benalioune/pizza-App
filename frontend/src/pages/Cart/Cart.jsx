import { useShop } from '../../contexts/ShopContext.jsx';
import { addOrder } from '../../services/api.js';
import styles from './Cart.module.scss';

export default function Cart() {
    const { cart, removeFromCart, clearCart } = useShop();
    const total = cart.reduce((s, p) => s + p.qty * p.price, 0);

    const checkout = async () => {
        if (!cart.length) return;
        await addOrder(cart, total);
        clearCart();
        alert('Commande enregistrée !');
    };

    return (
        <section className={styles.cart}>
            <h1>Votre panier</h1>

            {cart.length === 0 ? (
                <p>Le panier est vide.</p>
            ) : (
                <>
                    <table>
                        <thead>
                        <tr><th>Pizza</th><th>Qté</th><th>Prix</th><th></th></tr>
                        </thead>
                        <tbody>
                        {cart.map(p => (
                            <tr key={p.id}>
                                <td>{p.name}</td>
                                <td>{p.qty}</td>
                                <td>{(p.qty * p.price).toFixed(2)} €</td>
                                <td><button onClick={() => removeFromCart(p.id)}>✕</button></td>
                            </tr>
                        ))}
                        </tbody>
                    </table>

                    <p className={styles.total}>Total : {total.toFixed(2)} €</p>
                    <button className={styles.orderBtn} onClick={checkout}>
                        Passer commande
                    </button>
                </>
            )}
        </section>
    );
}
