students={
    "Rahul":85,
    "Sneha":92,
    "Arjun":78,
    "Priya":88
}

marks=list(students.values())
MaxMarks=max(marks)
for key,value in students.items():
    if value==MaxMarks:
        print("Name:",key)
        print("Marks:",MaxMarks)
avg=sum(marks)/len(marks)
print("Average Marks:",avg)
for key,value in students.items():
    if value>85:
        print(key,value)

