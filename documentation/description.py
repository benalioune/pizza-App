# API Description
api_description = """
🍕 Restaurant Management API 🚀

## Authentication

* Create an account (signup)
* Login to get access token
* View your profile information

## Todo List Features

* Create todos
* Get todo list
* Modify todos
* Delete todos

## Restaurant Management Features

### Menu Management (Admin Only)
* View the complete menu
* Add new pizzas to the menu
* Update existing pizzas
* Remove pizzas from the menu

### Order Management
* Place new orders with multiple items
* Track order status (reçue, en préparation, prête, livrée)
* Choose delivery type (sur place, à emporter, livraison)

### Table Management
* View all tables status
* Mark tables as occupied or free
* Link orders to tables

### Admin Features
* Update order status
* Manage menu items
* View and manage table status

## Role-Based Access
* Regular users can view menu and place orders
* Admin users can manage menu, orders, and tables
* Authentication required for most operations

## Technical Notes
* All admin operations require authentication with admin role
* Orders automatically check and update inventory
* Real-time database updates for order status
"""