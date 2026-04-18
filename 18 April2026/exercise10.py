logins=[
    ("Rahul","10:00"),
    ("Sneha","10:10"),
    ("Rahul","11:00"),
    ("Arjun","11:15"),
    ("Sneha","11:30")
]
names=[]

for line in logins:
    names.append(line[0])
print(names)

unique_names=list(set(names))
print(unique_names)

result=dict()

for name in unique_names:
    result[name]=names.count(name)

print(result)