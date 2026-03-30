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
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# ============================================================
# Task 1 — Explore the Menu
# ============================================================

print("\n===== MENU =====")

# We create category list manually
categories = ["Starters", "Mains", "Desserts"]

# First loop goes category by category
for cat in categories:

    print("\n===== ", cat, " =====")

    # Second loop checks each menu item
    for item in menu:

        details = menu[item]

        # Only print items that belong to current category
        if details["category"] == cat:

            # Convert True/False into readable text
            if details["available"] == True:
                status = "Available"
            else:
                status = "Unavailable"

            print(item, "₹" + str(details["price"]), "[" + status + "]")


# Count total items using loop
total_items = 0
for item in menu:
    total_items = total_items + 1

# Count only available items
available_items = 0
for item in menu:
    if menu[item]["available"] == True:
        available_items = available_items + 1

print("\nTotal items:", total_items)
print("Available items:", available_items)

# Find most expensive item manually
max_price = 0
max_item = ""

for item in menu:
    price = menu[item]["price"]

    if price > max_price:
        max_price = price
        max_item = item

print("Most expensive item:", max_item, max_price)

# Print items with price less than 150
print("\nItems under ₹150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(item, menu[item]["price"])


# ============================================================
# Task 2 — Cart Operations
# ============================================================

cart = []

# This function adds item to cart
def add_item(item, qty):

    # Check if item exists in menu
    if item not in menu:
        print("Item not found in menu")
        return

    # Check availability
    if menu[item]["available"] == False:
        print("Item is unavailable")
        return

    # Check if item is already present in cart so we update quantity instead of adding again
    # we do this to avoid duplicate entries in cart
    found = False

    for c in cart:
        if c["item"] == item:
            c["quantity"] = c["quantity"] + qty
            found = True

    # If not found, create new entry
    if found == False:
        new_item = {}
        new_item["item"] = item
        new_item["quantity"] = qty
        new_item["price"] = menu[item]["price"]

        cart.append(new_item)

# This function removes item from cart
def remove_item(item):

    found = False

    for c in cart:
        if c["item"] == item:
            cart.remove(c)
            found = True

    if found == False:
        print("Item not in cart")


# Perform given steps
add_item("Paneer Tikka", 2)
print("Current cart:", cart)

add_item("Gulab Jamun", 1)
print("Current cart:", cart)

add_item("Paneer Tikka", 1)
print("Current cart:", cart)

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)

remove_item("Gulab Jamun")
print("Current cart:", cart)


# Print order summary
print("\n========== Order Summary ==========")

subtotal = 0

# Calculate total price for each item
for c in cart:
    total = c["quantity"] * c["price"]
    subtotal = subtotal + total

    print(c["item"], "x", c["quantity"], "₹", total)

# Add GST and final amount
gst = subtotal * 0.05
total_pay = subtotal + gst

print("----------------------------------")
print("Subtotal:", subtotal)
print("GST (5%):", round(gst, 2))
print("Total Payable:", round(total_pay, 2))


# ============================================================
# Task 3 —  Inventory Tracker with Deep Copy
# ============================================================

import copy

# Create a deep copy so original data remains unchanged
inventory_backup = copy.deepcopy(inventory)

# Change one value to show difference
inventory["Paneer Tikka"]["stock"] = 5

print("\nChanged inventory:", inventory["Paneer Tikka"])
print("Backup inventory:", inventory_backup["Paneer Tikka"])

# Restore original data
inventory = copy.deepcopy(inventory_backup)

# Deduct stock based on cart
for c in cart:

    item = c["item"]
    qty = c["quantity"]

    if inventory[item]["stock"] >= qty:
        inventory[item]["stock"] = inventory[item]["stock"] - qty
    else:
        print("Not enough stock for", item)
        inventory[item]["stock"] = 0

# Check if stock is low
for item in inventory:

    stock = inventory[item]["stock"]
    level = inventory[item]["reorder_level"]

    if stock <= level:
        print("⚠ Reorder Alert:", item, "- only", stock, "left")

print("\nFinal Inventory:", inventory)
print("Backup Inventory:", inventory_backup)


# ============================================================
# Task 4 — Daily Sales Log Analysis
# ============================================================

# we go through each date and calculate total revenue manually
print("\nRevenue per day:")

revenues = {}

# Calculate total revenue for each day
for date in sales_log:

    orders = sales_log[date]
    total = 0

    for o in orders:
        total = total + o["total"]

    revenues[date] = total
    print(date, total)

# Find day with highest revenue
best_day = ""
max_val = 0

for d in revenues:
    if revenues[d] > max_val:
        max_val = revenues[d]
        best_day = d

print("Best day:", best_day)

# Count how many times each item appears
count = {}

for date in sales_log:

    orders = sales_log[date]

    for o in orders:
        for item in o["items"]:

            if item in count:
                count[item] = count[item] + 1
            else:
                count[item] = 1

# Find most ordered item
max_item = ""
max_count = 0

for item in count:
    if count[item] > max_count:
        max_count = count[item]
        max_item = item

print("Most ordered item:", max_item)

# Add new day data
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# Recalculate revenue after update
print("\nUpdated Revenue after adding new day:")

revenues = {}

for date in sales_log:

    orders = sales_log[date]
    total = 0

    for o in orders:
        total = total + o["total"]

    revenues[date] = total
    print(date, total)

# Find updated best day
best_day = ""
max_val = 0

for d in revenues:
    if revenues[d] > max_val:
        max_val = revenues[d]
        best_day = d

print("Updated Best day:", best_day)

# Print all orders one by one with numbering (we use simple counter instead of enumerate)
print("\nAll Orders:")

num = 1

for date in sales_log:

    orders = sales_log[date]

    for o in orders:
        print(num, ".", "[" + date + "]", "Order #", o["order_id"], "₹", o["total"], "Items:", o["items"])
        num = num + 1