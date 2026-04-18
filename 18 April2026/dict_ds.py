student={
    "name":"Rahul",
    "age":22,
    "course":"Python"
}

print(student)
print(student["name"])
print(student["age"])
print(student["course"])

#Get
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

#Add a new pair

student["city"]="Hyderabad"
print(student)