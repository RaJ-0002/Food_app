import json
from random import randint

class Admin:
    def __init__(self):
        self.food_items=dict()
    
    def generate_food_id(self):
        return str(randint(1234,9999))
    
    def add_food_items(self):
        food_id = self.generate_food_id()
        name = input("Food item name : ")
        quantity = input(" Quantity : ")
        price = float(input(" Price : "))
        discount = float(input(" Discount : "))
        stock = int(input(" Stock available : "))
        
        food_item = {
            "FoodID": food_id,
            "Name": name,
            "Quantity": quantity,
            "Price": price,
            "Discount": discount,
            "Stock": stock
        }
        self.food_items[food_id] = food_item
        self.save_to_json()
    
    def edit_food_items(self,food_id):
        if food_id in self.food_items:
            food_item = self.food_items[food_id]
            name = input("Food item name : ")
            quantity = input(" Quantity : ")
            price = float(input(" Price : "))
            discount = float(input(" Discount : "))
            stock = int(input(" Stock available : "))
            
            food_item = {
                "FoodID": food_id,
                "Name": name,
                "Quantity": quantity,
                "Price": price,
                "Discount": discount,
                "Stock": stock
            }
            self.food_items[food_id] = food_item
            self.save_to_json()
        
    def view_food_items(self):
        for food_item in self.food_items.values():
            print(json.dumps(food_item,indent = 4))
    
    def remove_food_item(self,food_id):
        if food_id in self.food_items:
            del self.food_items[food_id]
            self.save_to_json()
    
    def save_to_json(self):
        with open("food_items.json","w") as file:
            json.dump(self.food_items, file, indent=4)
    
    def load_from_json(self):
        try:
            with open("food_items.json","r") as file:
                self.food_items = json.load(file)
        except FileNotFoundError:
            self.food_items = {}
    
adm = Admin()
adm.load_from_json()
admin_input = input(" Type yes if you want to add food items : ")
if admin_input == "yes":
    print("Welcome :)")
    i=0
    num_of_items = int(input("Enter number of items you want to add : "))
    while i<num_of_items:
        adm.add_food_items()
        i+=1

admin_input = input(" Type yes if you want to edit food item : ")
if admin_input == "yes":
    food_id = input("enter food id you want to edit : ")
    adm.edit_food_items(food_id)

admin_input = input(" Type yes if you want to delete food item : ")
if admin_input == "yes":
    food_id = input("enter food id you want to delete : ")
    adm.remove_food_item(food_id)

adm.view_food_items()
print("*********JSON Representation*********")
print(json.dumps(adm.food_items,indent=4))