import csv

data=[
    ["name","marks"],
    ["Priya",88],
    ["Karen",75]
]

with open("output.csv","w") as file:
    writer=csv.writer(file)

    writer.writerows(data)