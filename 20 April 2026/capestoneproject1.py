import json
import csv 
#Part 1 Website Visit Analysis
visitors=[]
with open("website_visits.txt", "r") as file:
    for line in file:
        visitors.append(line.strip())

unique_visitors=list(set(visitors))
visitors_count=dict()
for visitor in unique_visitors:
    visitors_count[visitor]=visitors.count(visitor)
most_frequent_visitor=max(visitors_count, key=visitors_count.get)
print("All Visitors:", visitors)
print("Total number of visitors:", len(visitors))
print("Unique Visitors:", unique_visitors)
print("Visitor Counts:", visitors_count)
print("Most Frequent Visitor:", most_frequent_visitor, visitors_count[most_frequent_visitor])

#Part 2 Product Catalog Analysis
product_details=dict()
product_dict=dict()
with open("products.json", "r") as file:
    data=json.load(file)
    products=data["products"]
    for product in products:
        name=product["name"]
        price=product["price"]
        id=product["product_id"]
        product_details[name]=price
        product_dict[id]=dict()
        product_dict[id]["name"]=name
        product_dict[id]["price"]=price
most_expensive_product=max(product_details, key=product_details.get)
least_expensive_product=min(product_details, key=product_details.get)

print("Product names and prices:", product_details)
print("Product dictionary", product_dict)
print("Most Expensive Product:", most_expensive_product, product_details[most_expensive_product])
print("Least Expensive Product:", least_expensive_product, product_details[least_expensive_product])

#Part 3 Order Analysis 
order_list=[]
product_quantity=dict()
customer_order=dict()
with open("orders.csv", "r") as file:
    reader=csv.DictReader(file)
    for r in reader:
        order_list.append(r)
        name=r["customer"]
        quantity=int(r["quantity"])
        product_id=r["product_id"]
        product_quantity[product_id]=product_quantity.get(product_id,0)+quantity
        customer_order[name]=customer_order.get(name,0)+1
print("Orders:")
for order in order_list:
    print(order)
print("Total Quantity per product",product_quantity)
print("Total Order per customer",customer_order)

#Part 4 Sales Calculation
order_revenue=dict()
for order in order_list:
    order_id=order["order_id"]
    product_id=int(order["product_id"])
    quantity=int(order["quantity"])
    revenue=quantity*product_dict[product_id]["price"]
    order_revenue[order_id]=revenue
product_revenue=dict()
for key,value in product_quantity.items():
    name=product_dict[int(key)].get("name")
    price=product_dict[int(key)].get("price")
    product_revenue[name]=price*value
max_revenue=max(product_revenue, key=product_revenue.get)
total_revenue=sum(product_revenue.values())
print("Revenue per order:",order_revenue)
print("Total Revenue:",total_revenue)
print("Revenue per product:",product_revenue)
print("Highest Revenue:",max_revenue, product_revenue[max_revenue])

#Part 5 Customer Analysis
customer_spendings=dict()
for order in order_list:
    order_id=order["order_id"]
    name=order["customer"]
    customer_spendings[name]=customer_spendings.get(name,0)+order_revenue.get(order_id)
max_spent=max(customer_spendings, key=customer_spendings.get)
spent_more=[]
for key,value in customer_spendings.items():
    if value>50000:
        spent_more.append((key,value))
print("Total Spending per customer:",customer_spendings)
print("Highest Spending:",max_spent, customer_spendings[max_spent])
print("Customers spending more than Rs. 50,000:",spent_more)

#Part 6 Functions
def load_visits():
    visitors = []
    with open("website_visits.txt", "r") as file:
        for line in file:
            visitors.append(line.strip())
    return visitors
def load_product_catelog():
    product_catelog=dict()
    with open("products.json", "r") as file:
        data = json.load(file)
        products = data["products"]
        for product in products:
            name = product["name"]
            price = product["price"]
            id = product["product_id"]
            product_catelog[id] = dict()
            product_catelog[id]["name"] = name
            product_catelog[id]["price"] = price
    return product_catelog
def load_orders():
    orders=[]
    with open("orders.csv", "r") as file:
        reader= csv.DictReader(file)
        for r in reader:
            orders.append(r)
    return orders
def calculate_product_revenue():
    revenue=dict()
    orders=load_orders()
    product_catelog=load_product_catelog()
    for order in orders:
        product_id=int(order["product_id"])
        name=product_catelog[product_id]["name"]
        quantity=int(order["quantity"])
        price = quantity * product_catelog[product_id]["price"]
        revenue[name]=revenue.get(name,0)+price
    return revenue
def find_customer_spending():
    customer_spendings=dict()
    orders=load_orders()
    product_catelog=load_product_catelog()
    for order in orders:
        name=order["customer"]
        quantity = int(order["quantity"])
        product_id=int(order["product_id"])
        price=quantity*product_catelog[product_id]["price"]
        customer_spendings[name]=customer_spendings.get(name,0)+price
    return customer_spendings
def find_top_customers():
    customer_spendings=find_customer_spending()
    top_customer=(max(customer_spendings, key=customer_spendings.get),customer_spendings[max(customer_spendings, key=customer_spendings.get)])
    return top_customer

print("Visitors:", load_visits())
print("Product Categories:", load_product_catelog())
print("Orders:", load_orders())
print("Product Revenue:",calculate_product_revenue())
print("Customer Spendings",find_customer_spending())
print("Top Customer",find_top_customers())

#Part 8 Final Report Generattion
with open("sales_report.txt","w") as file:
    file.write("E-Commerce Sales Report\n")
    file.write(f"\nTotal Website Visits: {len(load_visits())}")
    file.write(f"\nUnique Visitors: {len(set(load_visits()))}\n")
    file.write(f"\nTotal Revenue: {sum(calculate_product_revenue().values())}\n")
    file.write(f"\nTop Customer: {find_top_customers()[0]}\n")
    file.write("\nProduct Sales")
    for key,values in calculate_product_revenue().items():
        file.write(f"\n{key} -> {str(values)}")

#Final Challenge
visitors=load_visits()
unique_visitors=set(visitors)
ordered_visitors=set(find_customer_spending().keys())
print("Visitors who never ordered anything:",list(unique_visitors.difference(ordered_visitors)))
ordered_once=[]
for keys,values in visitors_count.items():
    if not values>1:
        if keys in list(ordered_visitors):
            ordered_once.append((keys))
print("Visitors who ordered but never visited the website more than once:",ordered_once)
