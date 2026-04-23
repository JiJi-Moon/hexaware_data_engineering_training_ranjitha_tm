import json
import csv

from capestoneproject2 import eligible

#Part 1
students=[]
student_count=dict()
with open("students.txt","r") as f:
    for lines in f:
        students.append(lines.strip())
unique_students=set(students)
for student in unique_students:
    student_count[student]=students.count(student)
print("Total number of entries:",len(students))
print("Unique students:",unique_students)
print("Count of students in entries:",student_count)
with open("unique_students.txt","w") as f:
    for student in unique_students:
        f.write(student+"\n")

#Part 2
student_marks=dict()
student_course=dict()
python_students=[]
with open("marks.json","r") as f:
    data=json.load(f)
    marks=data["students"]
    for student in marks:
        name=student["name"]
        mark=student["marks"]
        course=student["course"]
        student_marks[name]=mark
        student_course[course]=student_course.get(course,0)+1
        if course=="Python":
            python_students.append(student["name"])
high_marks=max(student_marks,key=student_marks.get)
low_marks=min(student_marks,key=student_marks.get)
avg=sum(student_marks.values())/len(student_marks)
print("All students names and marks:",student_marks)
print("High marks:",high_marks,student_marks[high_marks])
print("Low marks:",low_marks,student_marks[low_marks])
print("Average marks:",avg)
print("Students enrolled in Python:",python_students)
print("Count of students in each course:",student_course)

#Part 3
student_attendance_details=[]
student_attendance=dict()
below_80=[]

with open("attendance.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        student_attendance_details.append(row)
        name=row["name"]
        present=int(row["days_present"])
        total=int(row["total_days"])
        percentage=(present/total)*100
        student_attendance[name]=percentage
        if percentage<80:
            below_80.append(name)
best_attendance=max(student_attendance,key=student_attendance.get)
print("Student Attendance Details:",student_attendance_details)
print("Student Attendance Percentage:",student_attendance)
print("Best attendance:",best_attendance,student_attendance[best_attendance])

#Part 4
marks_list=list(student_marks.values())
courses_tuple=tuple(student_course.keys())
unique_courses_set=set(courses_tuple)

print("Student Marks List",marks_list)
print("Highest Mark",max(marks_list))
print("Lowest Mark",min(marks_list))
print("Sum of Marks",sum(marks_list))
print("Courses in Tuple",courses_tuple)
print("Unique Courses in Set",unique_courses_set)
print("Student Marks Dictionary",student_marks)
print("Student Attendance Percentage Dictionary",student_attendance)

#Part 5
print("Student Pass or Fail details:")
for keys,values in student_marks.items():
    if values>=50:
        print(keys,values,"Pass")
    else:
        print(keys,values,"Fail")

student_grades=dict()
for keys,values in student_marks.items():
    if values>=90:
        student_grades[keys]="A"
    elif values>=75 and values<90:
        student_grades[keys]="B"
    elif values>=50 and values<75:
        student_grades[keys]="C"
    else:
        student_grades[keys]=("Fail")
print("Student Grades:",student_grades)
print("Students with Attendance above 85% and Marks above 80:")
for keys in list(student_marks.keys()):
    if student_marks[keys]>80 and student_attendance[keys]>=85:
        print(keys,student_marks[keys],student_attendance[keys])

#Part 6
def read_names(filename):
    students = []
    with open(filename, "r") as f:
        for lines in f:
            students.append(lines.strip())
    return students
def load_student_marks(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        marks = data["students"]
    return marks
def load_attendance(filename):
    attendance = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            attendance.append(row)
    return attendance
def calculate_average_marks():
    marks=load_student_marks("marks.json")
    marks_list=[]
    for mark in marks:
        marks_list.append(int(mark["marks"]))
    return sum(marks_list)/len(marks_list)
def cal_attendance_percentage():
    attendance=load_attendance("attendance.csv")
    attendance_percentage=dict()
    for att in attendance:
        name=att["name"]
        a=int(att["days_present"])
        b=int(att["total_days"])
        percent=a/b*100
        attendance_percentage[name]=percent
    return attendance_percentage
def find_topper():
    marks=load_student_marks("marks.json")
    marks_dict=dict()
    for mark in marks:
        stud_mark=mark["marks"]
        name=mark["name"]
        marks_dict[name]=stud_mark
    topper=max(marks_dict,key=marks_dict.get)
    return (topper,marks_dict[topper])
def generate_grade(mark):
    if mark>=90:
        return "A"
    elif mark>=75 and mark<90:
        return "B"
    elif mark>=50 and mark<75:
        return "C"
    else:
        return "Fail"

#Part 7
combined_marks=dict()
marks=load_student_marks("marks.json")
attendance=cal_attendance_percentage()
eligible=[]
improvement=[]
for row in marks:
    name=row["name"]
    mark=row["marks"]
    course=row["course"]
    attendance_percent=attendance[name]
    combined_marks[name]=dict()
    combined_marks[name]["marks"]=mark
    combined_marks[name]["course"]=course
    combined_marks[name]["attendance"]=attendance_percent
    if mark>=75 and attendance_percent>=80:
        eligible.append(name)
    else:
        improvement.append(name)
print("Combined Structure Dictionay:",combined_marks)
print("Combined Structure:")
for keys,values in combined_marks.items():
    print(f"Name: {keys}, Marks: {values["marks"]}, Attendance: {values['attendance']}, Course: {values['course']}, Grade: {generate_grade(values['marks'])}")
print("Eligible Students:",eligible)
print("Improvement needed Students:",improvement)

#Part 8
with open("report.txt","w") as f:
    f.write("Student Report:\n\n")
    for keys,values in combined_marks.items():
        f.write(f"{keys} - Marks: {values["marks"]} - Attendance: {values['attendance']}% - Grade: {generate_grade(values['marks'])}\n")
with open("eligible_students.txt","w") as f:
    for student in eligible:
        f.write(f"{student}\n")

#Final Challenge
topper=find_topper()[0]
attendance_percentage=cal_attendance_percentage()
best_attendance_percentage=max(attendance_percentage,key=attendance_percentage.get)
average_marks=calculate_average_marks()
print(f"Topper: {topper}")
print(f"Best Attendance: {best_attendance_percentage}")
print(f"Average Marks: {average_marks}")
print(f"Eligible Students: {eligible}")
print(f"Students Needing Improvement: {improvement}")