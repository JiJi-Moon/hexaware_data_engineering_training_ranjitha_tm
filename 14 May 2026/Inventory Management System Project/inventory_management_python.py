import csv
import pandas as pd
import numpy as np

products_data = [
    ['product_id', 'product_name', 'reorder_level'],
    [1, 'Laptop', 10],
    [2, 'Mouse', 20],
    [3, 'Keyboard', 15],
    [4, 'Monitor', 8],
    [5, 'Printer', 5],
    [6, 'Tablet', 12],
    [7, 'Speaker', 18],
    [8, 'Router', 10],
    [9, 'Hard Disk', 7],
    [10, 'Webcam', 9]
]

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(products_data)

stock_data = [
    ['movement_id', 'product_id', 'quantity', 'movement_type', 'movement_date'],
    [1, 1, 50, 'IN', '2026-01-10'],
    [2, 1, 10, 'OUT', '2026-01-18'],
    [3, 1, 20, 'IN', '2026-01-25'],
    [4, 2, 30, 'IN', '2026-01-12'],
    [5, 2, '', 'OUT', '2026-01-20'],  
    [6, 2, 5, 'OUT', '2026-01-28'],
    [7, 3, 20, 'IN', '2026-01-15'],
    [8, 3, -5, 'IN', '2026-01-22'], 
    [9, 3, 8, 'OUT', '2026-01-30'],
    [10, 4, 15, 'IN', 'invalid_date'], 
    [11, 4, 5, 'OUT', '2026-02-02'],
    [12, 5, 10, 'IN', '2026-02-05'],
    [13, 5, 6, 'OUT', '2026-02-08'],
    [14, 6, 25, 'IN', '2026-02-10'],
    [15, 6, 10, 'OUT', '2026-02-12'],
    [16, 7, 40, 'IN', '2026-02-01'],
    [17, 7, 30, 'OUT', '2026-02-03'],
    [18, 8, 12, 'IN', '2026-02-04'],
    [19, 8, 5, 'OUT', '2026-02-06'],
    [20, 9, 8, 'IN', '2026-02-07'],
    [21, 9, 2, 'OUT', '2026-02-09'],
    [22, 10, 18, 'IN', '2026-02-11'],
    [23, 10, 15, 'OUT', '2026-02-13']
]

with open('stock_movements.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(stock_data)

products = pd.read_csv("products.csv")
stock = pd.read_csv("stock_movements.csv")

print("raw stock data:\n", stock)

stock['quantity'] = pd.to_numeric(stock['quantity'], errors='coerce')
stock['quantity'] = stock['quantity'].fillna(0)
stock['quantity'] = np.clip(stock['quantity'], 0, None)

stock['movement_date'] = pd.to_datetime(stock['movement_date'], errors='coerce')
stock = stock.dropna(subset=['movement_date'])

print("\ncleaned stock data:\n", stock)

stock['adjusted_qty'] = np.where(
    stock['movement_type'] == 'OUT',
    -stock['quantity'],
    stock['quantity']
)

stock_summary = stock.groupby('product_id')['adjusted_qty'].sum().reset_index()
stock_summary.columns = ['product_id', 'current_stock']

print("\ncurrent stock:\n", stock_summary)

data = stock_summary.merge(products, on='product_id')

print("\nmerged data:\n", data)

low_stock = data[data['current_stock'] < data['reorder_level']]

print("\nlow stock products:\n", low_stock[['product_name', 'current_stock', 'reorder_level']])

avg_stock = np.mean(data['current_stock'])
print("\naverage stock:", avg_stock)

data.to_csv("current_stock.csv", index=False)
low_stock.to_csv("low_stock_report.csv", index=False)
