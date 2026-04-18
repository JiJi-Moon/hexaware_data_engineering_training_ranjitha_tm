import json
with open("students.json","r") as f:
    data = json.load(f)
students = data["students"]
names=[]
for student in students:
    names.append(student["name"])
pynames=[]
for student in students:
    if student["course"]=="Python":
        pynames.append(student["name"])

stu_marks=dict()
course_coutn=dict()
for student in students:
    name=student["name"]
    marks=student["marks"]
    course=student["course"]
    stu_marks[name]=marks
    course_coutn[course]=course_coutn.get(course,0)+1

print("All Students:",names)
print("Students Enrolled in Python:",pynames)
print("Highest Mark",stu_marks[max(stu_marks,key=stu_marks.get)])
print("Average marks",sum(stu_marks.values())/len(stu_marks))
print("Count of student is each course",course_coutn)


