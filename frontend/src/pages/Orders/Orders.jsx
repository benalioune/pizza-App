import React, { useEffect, useState } from "react";
import styles from "./Orders.module.scss";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";

const Orders = () => {
    const [orders, setOrders] = useState([]);
    useEffect(() => {
        fetch("localhost:8000/restau/orders", { method: "POST", body: JSON.stringify(setOrders)})
            .then(res => res.json())
            .then(setOrders);
    }, []);
    return (
        <div className={styles.orders}>
            <Header />
            <main>
                <h2>Mes commandes</h2>
                {orders.length === 0 ? (
                    <p>Aucune commande passée.</p>
                ) : (
                    <ul>
                        {orders.map(order => (
                            <li key={order.id}>
                                <b>Commande n°{order.id}</b> — {order.status} — {order.date}
                                <ul>
                                    {order.pizzas.map(pz => (
                                        <li key={pz.id}>{pz.nom} x {pz.qty}</li>
                                    ))}
                                </ul>
                            </li>
                        ))}
                    </ul>
                )}
            </main>
            <Footer />
        </div>
    );
};
export default Orders;
