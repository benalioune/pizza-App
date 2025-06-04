import { Routes, Route } from 'react-router-dom';
import Header from './components/Header/Header.jsx';
import Footer from './components/Footer/Footer.jsx';

import Home   from './pages/Home/Home.jsx';
import Pizzas from './pages/Pizzas/Pizzas.jsx';
import Cart   from './pages/Cart/Cart.jsx';
import Admin  from './pages/Admin/Admin.jsx';

export default function App() {
    return (
        <>
            <Header />
            <main style={{ paddingBottom: '2rem' }}>
                <Routes>
                    <Route path="/"        element={<Home />} />
                    <Route path="/pizzas"  element={<Pizzas />} />
                    <Route path="/cart"    element={<Cart />} />
                    <Route path="/admin/*" element={<Admin />} />
                </Routes>
            </main>
            <Footer />
        </>
    );
}
