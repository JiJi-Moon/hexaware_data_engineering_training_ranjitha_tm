numbers=[10,20,10,30,20,10,40]

unique_values=list(set(numbers))

unique_dict=dict()

for value in unique_values:
    unique_dict[value]=numbers.count(value)
print(unique_dict)
