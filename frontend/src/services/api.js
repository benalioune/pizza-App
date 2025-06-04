import axios from 'axios';
const api = axios.create({ baseURL: import.meta.env.VITE_API_URL });

// /* PIZZAS */
// export const getPizzas   = ()            => api.get('/pizzas').then(r=>r.data);
// export const addPizza    = (n,p)         => api.post('/pizzas',{name:n,price:p});
// export const updatePizza = (id,n,p)      => api.put(`/pizzas/${id}`,{name:n,price:p});
// export const deletePizza =  id           => api.delete(`/pizzas/${id}`);

// /* USERS */
// export const getUsers    = ()            => api.get('/users').then(r=>r.data);
// export const addUser     = (n,e)         => api.post('/users',{name:n,email:e});
// export const updateUser  = (id,n,e)      => api.put(`/users/${id}`,{name:n,email:e});
// export const deleteUser  =  id           => api.delete(`/users/${id}`);

// /* ORDERS */
// export const getOrders   = ()            => api.get('/orders').then(r=>r.data);
// export const addOrder    = (items,total) => api.post('/orders',{items,total});


/* PIZZAS */
export const getPizzas = () => api.get('/menu').then(r => r.data)
export const addPizza = (name, price, ingredients = []) =>
  api.post('/menu', { name, price, ingredients })

/* USERS */
export const signup = (email, password) =>
  api.post('/signup', { email, password })

export const login = (email, password) =>
  api.post('/login', new URLSearchParams({ username: email, password }))

// export const getMe = (token) =>
//   api.get('/me', { headers: { Authorization: `Bearer ${token}` } }).then(r => r.data)

/* ORDERS */
export const getOrders = () => api.get('/orders').then(r => r.data)
export const addOrder = (items, customer_name) =>
  api.post('/orders', { items, customer_name, total: calculateTotal(items) })

export const updateOrderStatus = (orderId, newStatus) =>
  api.patch(`/orders/${orderId}/status`, { new_status: newStatus })

/* TABLES */
export const getTables = () => api.get('/tables').then(r => r.data)
export const occupyTable = (tableId) => api.post(`/tables/${tableId}/occupy`)
