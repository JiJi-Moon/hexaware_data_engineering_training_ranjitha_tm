# PART 1 — Website Visit Analysis

# Task 1
with open("website_visits.txt","r") as f:
    visits = [line.strip() for line in f]

# Task 2
print(visits)

# Task 3
print(len(visits))

# Task 4
unique_visitors = set(visits)
print(unique_visitors)

# Task 5
visit_count = {}
for v in visits:
    visit_count[v] = visit_count.get(v, 0) + 1
print(visit_count)

# Task 6
most_visitor = max(visit_count, key=visit_count.get)
print(most_visitor)

# PART 2 — Product Catalog Analysis (JSON)

import json

# Task 7
with open("products.json") as f:
    products_data = json.load(f)["products"]

# Task 8
for p in products_data:
    print(p["name"], p["price"])

# Task 9
products = {
    p["product_id"]: {"name": p["name"], "price": p["price"]}
    for p in products_data
}
print(products)

# Task 10
expensive = max(products.values(), key=lambda x: x["price"])
print(expensive)

# Task 11
cheap = min(products.values(), key=lambda x: x["price"])
print(cheap)

# PART 3 — Orders Analysis (CSV)

import csv

# Task 12
orders = []
with open("orders.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["product_id"] = int(row["product_id"])
        row["quantity"] = int(row["quantity"])
        orders.append(row)

# Task 13
for o in orders:
    print(o)

# Task 14
qty_per_product = {}
for o in orders:
    pid = o["product_id"]
    qty_per_product[pid] = qty_per_product.get(pid, 0) + o["quantity"]
print(qty_per_product)

# Task 15
orders_per_customer = {}
for o in orders:
    c = o["customer"]
    orders_per_customer[c] = orders_per_customer.get(c, 0) + 1
print(orders_per_customer)

# PART 4 — Sales Calculation

# Task 16
for o in orders:
    price = products[o["product_id"]]["price"]
    revenue = price * o["quantity"]
    print(revenue)

# Task 17
total_revenue = 0
for o in orders:
    price = products[o["product_id"]]["price"]
    total_revenue += price * o["quantity"]
print(total_revenue)

# Task 18
revenue_per_product = {}
for o in orders:
    name = products[o["product_id"]]["name"]
    price = products[o["product_id"]]["price"]
    total = price * o["quantity"]
    revenue_per_product[name] = revenue_per_product.get(name, 0) + total
print(revenue_per_product)

# Task 19
top_product = max(revenue_per_product, key=revenue_per_product.get)
print(top_product)

# PART 5 — Customer Analysis

# Task 20
spending = {}
for o in orders:
    c = o["customer"]
    price = products[o["product_id"]]["price"]
    total = price * o["quantity"]
    spending[c] = spending.get(c, 0) + total
print(spending)

# Task 21
top_customer = max(spending, key=spending.get)
print(top_customer)

# Task 22
high_spenders = [c for c, amt in spending.items() if amt > 50000]
print(high_spenders)

# PART 6 — Functions

# Task 23
def load_visits(file):
    with open(file) as f:
        return [line.strip() for line in f]

# Task 24
def load_products(file):
    import json
    with open(file) as f:
        data = json.load(f)["products"]
        return {p["product_id"]: p for p in data}

# Task 25
def load_orders(file):
    import csv
    orders = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["product_id"] = int(row["product_id"])
            row["quantity"] = int(row["quantity"])
            orders.append(row)
    return orders


# Task 26
def product_revenue(orders, products):
    revenue = {}
    for o in orders:
        name = products[o["product_id"]]["name"]
        price = products[o["product_id"]]["price"]
        total = price * o["quantity"]
        revenue[name] = revenue.get(name, 0) + total
    return revenue


# Task 27
def customer_spending(orders, products):
    spending = {}
    for o in orders:
        customer = o["customer"]
        price = products[o["product_id"]]["price"]
        total = price * o["quantity"]
        spending[customer] = spending.get(customer, 0) + total
    return spending


# Task 28
def top_customer_func(spending):
    return max(spending, key=spending.get)

# PART 7 — Data Structures

orders = load_orders("orders.csv")
products = load_products("products.json")
visits = load_visits("website_visits.txt")

product_prices = {pid: data["price"] for pid, data in products.items()}
unique_visitors = set(visits)

revenue_per_product = product_revenue(orders, products)
product_revenue_pairs = [(name, rev) for name, rev in revenue_per_product.items()]

print(orders)
print(product_prices)
print(unique_visitors)
print(product_revenue_pairs)

# PART 8 — Final Report Generation

with open("sales_report.txt", "w") as f:
    f.write("E-Commerce Sales Report\n")
    f.write(f"Total Website Visits: {len(visits)}\n")
    f.write(f"Unique Visitors: {len(unique_visitors)}\n")
    f.write(f"Total Revenue: {total_revenue}\n\n")
    f.write(f"Top Customer: {top_customer}\n")
    f.write("Product Sales\n")
    for p, rev in revenue_per_product.items():
        f.write(f"{p} -> {rev}\n")

# FINAL CHALLENGE

# Task 29
visitors_no_order = unique_visitors - set(spending.keys())
print(visitors_no_order)

# Task 30
visit_count = {}
for v in visits:
    visit_count[v] = visit_count.get(v, 0) + 1

ordered_customers = set(spending.keys())
result = []

for c in ordered_customers:
    if visit_count.get(c, 0) <= 1:
        result.append(c)

print(result)