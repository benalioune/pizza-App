import React, { useEffect, useState } from "react";
import styles from "./OrdersAdmin.module.scss";
import Header from "../../../components/Header/Header";
import Footer from "../../../components/Footer/Footer";

const OrdersAdmin = () => {
    const [orders, setOrders] = useState([]);
    useEffect(() => {
        fetch("localhost:8000/restau/menu",  {method: "POST", body: JSON.stringify(setOrders)})
        .then(res=>res.json())
        .then(setOrders);
    }, []);
    return (
        <div className={styles.ordersAdmin}>
            <Header admin />
            <main>
                <h2>Admin — Commandes</h2>
                <ul>
                    {orders.map(order => (
                        <li key={order.id}>
                            <b>Commande n°{order.id}</b> — {order.status}
                            <ul>
                                {order.pizzas.map(pz => (
                                    <li key={pz.id}>{pz.nom} x {pz.qty}</li>
                                ))}
                            </ul>
                        </li>
                    ))}
                </ul>
            </main>
            <Footer />
        </div>
    );
};
export default OrdersAdmin;
