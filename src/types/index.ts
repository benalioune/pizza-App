export interface Pizza {
    id: string;
    name: string;
    price: number;
    ingredients: string[];
    size: string;
}

export interface Order {
    id: string;
    customer_name: string;
    items: OrderItem[];
    status: string;
    order_time: string;
}

export interface OrderItem {
    pizza_id: string;
    quantity: number;
}

export interface Table {
    id: string;
    status: string;
    order_id: string | null;
}

export interface User {
    email: string;
    uid: string;
    role?: string;
    created_at?: string;
}

export interface AuthResponse {
    access_token: string;
    token_type: string;
} 