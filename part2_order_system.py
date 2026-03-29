# Part 2: Data Structures
# Theme: Restaurant Menu & Order Management System

# ============================================================
# Provided Data (as given)
# ============================================================

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price": 40.0,  "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price": 90.0,  "available": True},
    "Rasgulla":       {"category": "Desserts",  "price": 80.0,  "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock": 8,  "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock": 6,  "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock": 5,  "reorder_level": 2},
    "Rasgulla":       {"stock": 4,  "reorder_level": 3},
    "Ice Cream":      {"stock": 7,  "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7, "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8, "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9, "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}


# ============================================================
# Task 1 — Explore the Menu
# ============================================================

print("\n===== MENU =====")

# get all categories from menu so we can print category wise
categories = set([item["category"] for item in menu.values()])

# loop through each category and print the items
for cat in categories:
    print(f"\n===== {cat} =====")
    for name, details in menu.items():
        # check category and print matching items
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:15} ₹{details['price']}   [{status}]")

# calculate basic statistics like total items and available items
total_items = len(menu)
available_items = sum(1 for i in menu.values() if i["available"])

print("\nTotal items:", total_items)
print("Available items:", available_items)

# find the most expensive item in the menu
exp_item = max(menu.items(), key=lambda x: x[1]["price"])
print("Most expensive:", exp_item[0], exp_item[1]["price"])

# print items which have price less than 150
print("\nItems under ₹150:")
for name, details in menu.items():
    if details["price"] < 150:
        print(name, details["price"])


# ============================================================
# Task 2 — Cart Operations
# ============================================================

# create an empty cart to store items
cart = []

# function to add item in cart
def add_item(item, qty):
    # check if item exists in menu
    if item not in menu:
        print("Item not in menu")
        return
    # check if item is available
    if not menu[item]["available"]:
        print("Item unavailable")
        return

    # if item already in cart then just increase quantity
    for c in cart:
        if c["item"] == item:
            c["quantity"] += qty
            return

    # otherwise add new item
    cart.append({"item": item, "quantity": qty, "price": menu[item]["price"]})

# function to remove item from cart
def remove_item(item):
    # search item in cart and remove it
    for c in cart:
        if c["item"] == item:
            cart.remove(c)
            return
    print("Item not in cart")

# try adding and removing items in cart
add_item("Paneer Tikka", 2)
print(cart)

add_item("Gulab Jamun", 1)
print(cart)

add_item("Paneer Tikka", 1)
print(cart)

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)

remove_item("Gulab Jamun")
print(cart)

# print final order summary with total amount
print("\n========== Order Summary ==========")

# calculate total amount for all items in cart
subtotal = 0

# loop through cart items to calculate total
for c in cart:
    # calculate total for each item
    total = c["quantity"] * c["price"]
    subtotal += total
    print(f"{c['item']:15} x{c['quantity']} ₹{total}")

gst = subtotal * 0.05
total_pay = subtotal + gst

print("--------------------------------")
print("Subtotal:", subtotal)
print("GST:", round(gst,2))
print("Total:", round(total_pay,2))


# ============================================================
# Task 3 — Inventory Tracker with Deep Copy
# ============================================================

import copy

# creating backup using deep copy
inventory_backup = copy.deepcopy(inventory)

# change one value to check that backup is not affected
inventory["Paneer Tikka"]["stock"] = 5

print("\nChanged inventory:", inventory["Paneer Tikka"])
print("Backup inventory:", inventory_backup["Paneer Tikka"])

# restoring original inventory
inventory = copy.deepcopy(inventory_backup)

# deduct stock based on cart
for c in cart:
    item = c["item"]
    qty = c["quantity"]

    # reduce stock after order
    if inventory[item]["stock"] >= qty:
        inventory[item]["stock"] -= qty
    else:
        print("Low stock for", item)
        # if stock is less, deduct whatever is available (not below 0)
        inventory[item]["stock"] = max(0, inventory[item]["stock"] - qty)
        
# check if stock is low and print alert
for name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print("⚠ Reorder Alert:", name, details["stock"])

# print final inventory and backup to compare
print("\nFinal Inventory:", inventory)
print("Backup Inventory:", inventory_backup)


# ============================================================
# Task 4 — Daily Sales Log Analysis
# ============================================================

print("\nRevenue per day:")

# store revenue for each day
revenues = {}

# calculate revenue for each day
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    revenues[date] = total
    print(date, total)

# find the day with highest total revenue (best day)
best_day = max(revenues, key=revenues.get)
print("Best day:", best_day)

# count how many times each item is ordered
count = {}

# find most ordered item
for orders in sales_log.values():
    # go through all orders and their items
    for o in orders:
        for item in o["items"]:
            count[item] = count.get(item, 0) + 1

most_ordered = max(count, key=count.get)
print("Most ordered item:", most_ordered)

# add a new day to sales log to update data
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nAll Orders:")
# print all orders using numbering
i = 1
for date, orders in sales_log.items():
    for o in orders:
        print(f"{i}. [{date}] Order #{o['order_id']} ₹{o['total']} Items: {', '.join(o['items'])}")
        i += 1