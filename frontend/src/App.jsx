import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Import pages
import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import Pizzas from "./pages/Pizzas/Pizzas";
import PizzaDetails from "./pages/PizzaDetails/PizzaDetails";
import Cart from "./pages/Cart/Cart";
import Checkout from "./pages/Checkout/Checkout";
import Orders from "./pages/Orders/Orders";
import Profile from "./pages/Profile/Profile";
import About from "./pages/About/About";
import Contact from "./pages/Contact/Contact";
import NotFound from "./pages/NotFound/NotFound";

// Import admin pages
import Dashboard from "./pages/admin/Dashboard/Dashboard";
import PizzasAdmin from "./pages/admin/PizzasAdmin/PizzasAdmin";
import AddPizza from "./pages/admin/AddPizza/AddPizza";
import EditPizza from "./pages/admin/EditPizza/EditPizza";
import OrdersAdmin from "./pages/admin/OrdersAdmin/OrdersAdmin";
import UsersAdmin from "./pages/admin/UsersAdmin/UsersAdmin";
import TodosAdmin from "./pages/admin/TodosAdmin/TodosAdmin";

const App = () => (
    <Router>
        <Routes>
            {/* Pages publiques/utilisateur */}
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/pizzas" element={<Pizzas />} />
            <Route path="/pizzas/:id" element={<PizzaDetails />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/checkout" element={<Checkout />} />
            <Route path="/orders" element={<Orders />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />

            {/* Pages admin */}
            <Route path="/admin/dashboard" element={<Dashboard />} />
            <Route path="/admin/pizzas" element={<PizzasAdmin />} />
            <Route path="/admin/pizzas/add" element={<AddPizza />} />
            <Route path="/admin/pizzas/:id/edit" element={<EditPizza />} />
            <Route path="/admin/orders" element={<OrdersAdmin />} />
            <Route path="/admin/users" element={<UsersAdmin />} />
            <Route path="/admin/todos" element={<TodosAdmin />} />

            {/* 404 */}
            <Route path="*" element={<NotFound />} />
        </Routes>
    </Router>
);

export default App;
