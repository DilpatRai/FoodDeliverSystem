class FoodDeliverySystem:
    order_id = 0
    orders_log = {}
    def __init__(self):
        self.menu = {
            "Burger": 100,
            "Pizza": 200,
            "Pasta": 150,
            "French Fries": 50,
            "Sandwich": 80
        }
        self.bill_amount = 0
    def display_menu(self):
       # return self.menu
        for item in self.menu:
            print(item, "|", self.menu[item])
    def place_order(self, customer_name, order_items):
        # returns order_log  # order_id, customer_name, order_items, status
        FoodDeliverySystem.order_id += 1
        FoodDeliverySystem.orders_log[FoodDeliverySystem.order_id] = {"customer_name": customer_name, "order_items": order_items, "status": "Placed"}
        return FoodDeliverySystem.orders_log
    def pick_up_order(self, order_id):
        # returns status
        if order_id in FoodDeliverySystem.orders_log:
            FoodDeliverySystem.orders_log[order_id]["status"] = "Picked Up"
            return FoodDeliverySystem.orders_log[order_id]["status"]
        else:
            return "Order Not Found"
    def delivery_order(self, order_id):
        # returns status
        if order_id in FoodDeliverySystem.orders_log:
            FoodDeliverySystem.orders_log[order_id]["status"] = "Delevered"
            return FoodDeliverySystem.orders_log[order_id]["status"]
        else:
            return "Order Not Found"
    def modify_order(self, order_id, new_items):
        # returns order_log
        if order_id in FoodDeliverySystem.orders_log:
            FoodDeliverySystem.orders_log[order_id]["order_items"] = new_items
            return FoodDeliverySystem.orders_log
        else:
            return "Order Not Found"
    def generate_bil(self, order_id):
        # returns bill_amount
        # if sum of order_items in orders_log[order_id] is greater than 1000, then add 10% tax
        # if sum of order_items in orders_log[order_id] is less than 1000, then 5% tax
        if order_id in FoodDeliverySystem.orders_log:
            self.bill_amount = sum([self.menu[item] for item in FoodDeliverySystem.orders_log[order_id]["order_items"]])
            if self.bill_amount > 1000:
                self.bill_amount += self.bill_amount * 0.1
            else:
                self.bill_amount += self.bill_amount * 0.05
            return self.bill_amount
        else:
            return "Order Not Found"
    def cancel_order(self, order_id):
        # cancel the order if not picked up 
        # returns status
        if order_id in FoodDeliverySystem.orders_log:
            if FoodDeliverySystem.orders_log[order_id]["status"] == "Placed":
                FoodDeliverySystem.orders_log[order_id]["status"] = "Cancelled"
                return FoodDeliverySystem.orders_log[order_id]["status"]
            else:
                return "Order Already Picked Up"
        else:
            return "Order Not Found"

# Path: main.py
from food import FoodDeliverySystem
food = FoodDeliverySystem()
print(food.display_menu())
print(food.place_order("John", ["Burger", "Pizza"]))
print(food.pick_up_order(1))
print(food.delivery_order(1))
print(food.modify_order(1, ["Pasta", "French Fries"]))
print(food.generate_bil(1))
print(food.cancel_order(1))

