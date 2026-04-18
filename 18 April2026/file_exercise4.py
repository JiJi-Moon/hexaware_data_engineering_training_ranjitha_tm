import json

from April18.exercise11 import customer

with open("orders.json","r") as f:
    data=json.load(f)
orders=data["orders"]

customers=dict()
order_details=dict()

for order in orders:
    customer=order["customer"]
    amount=order["amount"]
    customers[customer]=customers.get(customer,0)+amount
    order_details[customer]=order_details.get(customer,0)+1

print("All orders:",orders)
print("Total revenue",sum(customers.values()))
print("Total spendings per customer",customers)
print("Highest spending customer",max(customers,key=customers.get),customers[max(customers,key=customers.get)])
print("Total orders per customer",order_details)