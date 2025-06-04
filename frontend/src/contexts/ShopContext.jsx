import { createContext, useContext, useState } from 'react';

const Ctx = createContext();
export const useShop = () => useContext(Ctx);

export function ShopProvider({ children }) {
    const [cart, setCart] = useState([]);

    const addToCart = pizza =>
        setCart(c =>
            c.find(i => i.id === pizza.id)
                ? c.map(i => i.id === pizza.id ? { ...i, qty: i.qty + 1 } : i)
                : [...c, { ...pizza, qty: 1 }]
        );

    const removeFromCart = id => setCart(c => c.filter(i => i.id !== id));
    const clearCart      = ()  => setCart([]);

    return (
        <Ctx.Provider value={{ cart, addToCart, removeFromCart, clearCart }}>
            {children}
        </Ctx.Provider>
    );
}
