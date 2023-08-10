import json

class User:
    
    def __init__(self):
        self.users_details = dict()
        self.orders = list()
    
    def register(self):
        full_name = input("Please enter you name : ")
        phone_number = int(input("Enter phone number : "))
        email = input("Please enter email : ")
        address = input("Enter the address : ")
        password = input("Please enter the password : ")
        
        user_details = {
            "full_name":full_name,
            "phone_number":phone_number,
            "email":email,
            "address":address,
            "password":password
        }
        self.users_details[email]=user_details
        self.save_users_to_json()
    
    def login(self):
        email = input("Email: ")
        if email in self.users_details:
            password = input("Password: ")
            if self.users_details[email]["password"] == password:
                return email
        return None

    def place_new_order(self, user_id):
        print("Available Food Items:")
        food_items = {
            1: "Tandoori Chicken (4 pieces) [INR 240]",
            2: "Vegan Burger (1 Piece) [INR 320]",
            3: "Truffle Cake (500gm) [INR 900]"
        }
        for item_id, item in food_items.items():
            print(f"{item_id}. {item}")
        
        selected_items = input("Enter array of numbers for selected items (e.g., 2,3): ")
        selected_items = [int(item_id.strip()) for item_id in selected_items.split(",")]
        
        order = {}
        for item_id in selected_items:
            quantity = int(input(f"Enter quantity for item {item_id}: "))
            order[item_id] = quantity
        
        self.orders.append({"User": user_id, "Order": order})
        self.save_orders_to_json()
            
    def order_history(self, user_id):
        print("Order History:")
        user_orders = [order for order in self.orders if order["User"] == user_id]
        for order in user_orders:
            print(json.dumps(order["Order"], indent=4))


    def edit_user_details(self,email):
        if email in self.users_details:
            user_details = self.users_details[user_details]
            full_name = input("Please enter you name : ")
            phone_number = int(input("Enter phone number : "))
            email = input("Please enter email : ")
            address = input("Enter the address : ")
            password = input("Please enter the password : ")
            
            user_details = {
                "full_name":full_name,
                "phone_number":phone_number,
                "email":email,
                "address":address,
                "password":password
            }
        self.users_details[email]=user_details
        self.save_users_to_json()
        

    def save_users_to_json(self):
        with open("users_details.json","w") as file:
            json.dump(self.users_details,file,indent=4)
        
        
    def load_users_from_json(self):
        try:
            with open("users_details.json", "r") as file:
                self.users_details = json.load(file)
        except FileNotFoundError:
            self.users_details = {}
    
    def save_orders_to_json(self):
        with open("orders_details.json","w") as file:
            json.dump(self.orders,file, indent = 4)
    
    def load_orders_from_json(self):
        try:
            with open("orders_details.json", "r") as file:
                self.orders_details = json.load(file)
        except FileNotFoundError:
            self.orders_details = []
            

                
user_app = User()
user_app.load_users_from_json()
user_app.load_orders_from_json()

while True:
    print("\nUser Functionalities:")
    print("1. Register")
    print("2. Log in")
    print("3. Place New Order")
    print("4. Order History")
    print("5. Update Profile")
    print("6. Exit")

    user_input=input(" Enter your choice : ")
    if user_input == "1":
        user_app.register()
    elif user_input == "2":
        user_id=user_app.login()
        if user_id is not None:
                print("Login Successful!")

                while True:
                    print("\nUser Options:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Log Out")

                    user_choice = input("Enter the choice")

                    if user_choice == "1":
                        user_app.place_new_order(user_id)
                    elif user_choice == "2":
                        user_app.order_history(user_id)
                    elif user_choice == "3":
                        user_app.edit_user_details(user_id)
                    elif user_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        else:
            print("Invalid credintials")
    elif user_input == "3":
        print("You need to log in to place an order.")
    elif user_input == "4":
        print("You need to log in to view order history.")
    elif user_input == "5":
        print("You need to log in to update your profile.")
    elif user_input == "6":
        print("Successfully logged out......:) \n You are always welcome \n _________/\_________")
        break
        