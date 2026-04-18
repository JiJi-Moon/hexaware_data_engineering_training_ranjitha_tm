orders=[
    {"order_id":1,"customer":"Rahul","amount":2500},
    {"order_id":2,"customer":"Sneha","amount":1800},
    {"order_id":3,"customer":"Rahul","amount":3200},
    {"order_id":4,"customer":"Amit","amount":1500},
]
total_spending=dict()
total_orders=dict()

for order in orders:
    customer=order["customer"]
    amount=order["amount"]
    total_spending[customer]=total_spending.get(customer,0)+amount
    total_orders[customer]=total_orders.get(customer,0)+1

print(total_spending)

MaxSpending=max(total_spending,key=total_spending.get)
print("Higest spending customer:",MaxSpending,total_spending[MaxSpending])

print(total_orders)
