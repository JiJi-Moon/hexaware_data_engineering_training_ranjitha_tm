numbers=[]
with open("numbers.txt","r") as f:
    for line in f:
        numbers.append(int(line.strip()))

count_greater=0
for i in numbers:
    if i>50:
        count_greater+=1
print("Sum of all numbers:",sum(numbers))
print("Maximum of all numbers:",max(numbers))
print("Minimum of all numbers:",min(numbers))
print("Count of numbers greater than 50:",count_greater)