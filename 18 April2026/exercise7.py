products={
    "Laptop":75000,
    "Mobile":30000,
    "Tablet":25000
}

print(products)

for key,value in products.items():
    products[key]=value+(value*0.10)

print(products)
