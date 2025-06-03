from database.firebase import db, authTodo
import uuid

def init_database():
    try:
        # Login as admin
        user = authTodo.sign_in_with_email_and_password("test3@example.com", "password123")
        # Get the ID token
        id_token = user['idToken']
        
        # Initialize menu with some pizzas
        pizzas = [
            {
                "id": str(uuid.uuid4()),
                "name": "Margherita",
                "price": 10.99,
                "ingredients": ["tomato sauce", "mozzarella", "basil"],
                "size": "M"
            },
            {
                "id": str(uuid.uuid4()),
                "name": "Pepperoni",
                "price": 12.99,
                "ingredients": ["tomato sauce", "mozzarella", "pepperoni"],
                "size": "M"
            }
        ]
        
        # Add pizzas to menu
        for pizza in pizzas:
            db.child("menu").child(pizza["id"]).set(pizza, token=id_token)
        
        # Initialize tables
        tables = {
            "table1": {"status": "libre", "order_id": None},
            "table2": {"status": "libre", "order_id": None},
            "table3": {"status": "libre", "order_id": None}
        }
        
        # Add tables
        db.child("tables").set(tables, token=id_token)
        
        # Initialize inventory
        inventory = {
            "tomato sauce": 100,
            "mozzarella": 100,
            "basil": 50,
            "pepperoni": 50
        }
        
        # Add inventory
        db.child("inventory").set(inventory, token=id_token)
        
        # Set user role as admin
        db.child("users").child(user['localId']).update({"role": "admin"}, token=id_token)
        
        print("Database initialized successfully!")
        
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

if __name__ == "__main__":
    init_database() 