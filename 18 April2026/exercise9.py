sales=[
    {"product":"Laptop","qty":5},
    {"product":"Mouse","qty":20},
    {"product":"Laptop","qty":3},
    {"product":"Keyboard","qty":10}
]
product_total=dict()

for p in sales:
    name=p["product"]
    qty=p["qty"]
    product_total[name]=product_total.get(name,0)+qty

print(product_total)

MaxSelling=max(product_total,key=product_total.get)
print("Highest Selling Product:",MaxSelling,product_total[MaxSelling])
