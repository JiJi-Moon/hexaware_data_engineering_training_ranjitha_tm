import json
with open("data.json","r") as file:
    data=json.load(file)

print(data)
for student in data["students"]:
    print(student["name"],student["marks"])

#Write

students = {
    "students": [
        {"name":"Priya", "marks": 88},
        {"name":"Karen", "marks": 75},
    ]
}

with open("output.json","w") as file:
    json.dump(students,file)

#Write operation with pretty output

with open("output1.json","w") as file:
    json.dump(students,file,indent=4)