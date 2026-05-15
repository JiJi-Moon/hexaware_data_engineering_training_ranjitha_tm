import pandas as pd
from datetime import datetime

start_time = datetime.now()
print("pipeline started at", start_time)

df = pd.read_csv("inventory_csv")

df['current_stock'] = df['current_stock'].fillna(0)
df['current_stock'] = df['current_stock'].clip(lower=0)

low_stock = df[df['current_stock'] < df['reorder_level']]

low_stock.to_csv("daily_low_stock_report.csv", index=False)

end_time = datetime.now()

print("total products flagged:", len(low_stock))
print("pipeline completed at", end_time)
