import axios from 'axios';
import { Pizza, Order, Table, AuthResponse, User } from '../types';

const API_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const authAPI = {
    login: async (email: string, password: string): Promise<AuthResponse> => {
        const formData = new FormData();
        formData.append('username', email);
        formData.append('password', password);
        const response = await api.post<AuthResponse>('/auth/login', formData);
        return response.data;
    },

    signup: async (email: string, password: string): Promise<{ message: string; user_id: string }> => {
        const response = await api.post('/auth/signup', { email, password });
        return response.data;
    },

    getCurrentUser: async (): Promise<User> => {
        const response = await api.get('/auth/me');
        return response.data;
    },
};

export const menuAPI = {
    getMenu: async (): Promise<Pizza[]> => {
        const response = await api.get('/restaurant/menu');
        return response.data;
    },

    addPizza: async (pizza: Omit<Pizza, 'id'>): Promise<Pizza> => {
        const response = await api.post('/restaurant/menu', pizza);
        return response.data;
    },
};

export const orderAPI = {
    createOrder: async (order: Omit<Order, 'id' | 'status' | 'order_time'>): Promise<Order> => {
        const response = await api.post('/restaurant/orders', order);
        return response.data;
    },

    updateOrderStatus: async (orderId: string, status: string): Promise<{ message: string }> => {
        const response = await api.patch(`/restaurant/orders/${orderId}/status`, { new_status: status });
        return response.data;
    },
};

export const tableAPI = {
    getTables: async (): Promise<Record<string, Table>> => {
        const response = await api.get('/restaurant/tables');
        return response.data;
    },

    occupyTable: async (tableId: string): Promise<void> => {
        await api.post(`/restaurant/tables/${tableId}/occupy`);
    },
}; 