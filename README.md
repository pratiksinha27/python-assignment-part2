# Python Assignment - Part 2

**Student ID:** BITSoM_BA_2511504

---

## Restaurant Menu & Order Management System

This assignment demonstrates the use of Python data structures such as dictionaries, lists, and nested data handling.
The program simulates a basic **Restaurant Order Management System** that manages menu items, customer orders, inventory, and sales analysis.

---

## Task Breakdown

### Task 1 — Menu Exploration

* Displays menu grouped by category (Starters, Mains, Desserts)
* Shows item price and availability status
* Calculates total number of items
* Calculates number of available items
* Finds the most expensive item
* Lists all items priced under ₹150

---

### Task 2 — Cart Operations

* Simulates a customer placing an order step by step
* Adds items to cart with validation
* Updates quantity if item already exists in cart
* Handles unavailable and invalid items
* Removes items from cart
* Updates item quantity
* Generates a formatted order summary with:

  * Subtotal
  * GST (5%)
  * Total payable amount

---

### Task 3 — Inventory Tracker with Deep Copy

* Uses `copy.deepcopy()` to create a backup of inventory
* Demonstrates difference between original and copied data
* Restores original inventory after modification
* Deducts stock based on customer order
* Handles insufficient stock cases
* Displays reorder alerts when stock reaches reorder level

---

### Task 4 — Sales Log Analysis

* Calculates total revenue per day
* Identifies the best-performing day
* Finds the most ordered item across all orders
* Adds a new day's data and updates results
* Displays all orders using `enumerate()` in a structured format

---

## Concepts Used

* **Data Structures**: Dictionaries, Lists, Nested Data
* **Loops**: `for` loops
* **Conditionals**: `if`, `else`
* **Functions**: Custom functions for cart operations
* **String Formatting**: f-strings, alignment using `ljust()`
* **Copying Data**: `copy.deepcopy()`
* **Enumeration**: `enumerate()`

---

## How to Run

1. Open the file `part2_order_system.py` in VS Code or any Python IDE
2. Run the program
3. View the output in the terminal

---

## Output

The program will display:

* Menu grouped by categories
* Cart updates after each operation
* Final order summary with bill details
* Inventory changes and reorder alerts
* Revenue per day and best day
* Most ordered item
* List of all orders with numbering

---

## Author

**Pratik Sinha**
