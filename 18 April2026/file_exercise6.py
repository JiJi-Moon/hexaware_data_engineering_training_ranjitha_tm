import csv
sales=dict()
quanties=dict()
with open("sales.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        product=row["product"]
        price=int(row["price"])
        qantity=int(row["quantity"])
        sales[product]=sales.get(product,0)+price
        quanties[product]=quanties.get(product,0)+qantity

print("Total Sales Revenue",sum(sales.values()))
print("Total Quantity per product:",quanties)
print("Total Sales Total:",max(sales,key=sales.get),max(sales.values()))
print("Total Revenue per product:",sales)
print("Product sales above 50,000:",end="\t")
for key,values in sales.items():
    if values>50000:
        print(key,values)
products=list(sales.keys())
print("Product Sales Summary")
for i in products:
    print(i,"->","Qty:",quanties[i],"Revenue:",sales[i])

