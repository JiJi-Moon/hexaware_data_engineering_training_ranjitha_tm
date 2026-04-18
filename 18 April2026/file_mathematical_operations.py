# perform mathematical operations
total = 0

with open("data1.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total:", total)