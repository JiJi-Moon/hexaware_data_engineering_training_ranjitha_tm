# ================================
# PART 1 — Basics and File Handling
# ================================

# Task 1: Read students.txt
with open("students.txt", "r") as f:
    data = f.readlines()

# Task 1: Print student names
for name in data:
    print(name.strip())

# Task 2: Total students
print(len(data))

# Task 3: Unique students
unique_students = set([name.strip() for name in data])
print(unique_students)

# Task 4: Count occurrences
count_dict = {}
for name in data:
    name = name.strip()
    count_dict[name] = count_dict.get(name, 0) + 1
print(count_dict)

# Task 5: Write unique students to file
with open("unique_students.txt", "w") as f:
    for name in unique_students:
        f.write(name + "\n")


# ================================
# PART 2 — JSON Handling
# ================================

import json

# Task 6: Read marks.json
with open("marks.json", "r") as f:
    marks_data = json.load(f)["students"]

# Task 7: Print names and marks
for s in marks_data:
    print(s["name"], s["marks"])

# Task 8: Find topper
topper = max(marks_data, key=lambda x: x["marks"])
print(topper)

# Task 9: Find lowest
lowest = min(marks_data, key=lambda x: x["marks"])
print(lowest)

# Task 10: Average marks
marks_list = [s["marks"] for s in marks_data]
avg = sum(marks_list) / len(marks_list)
print(avg)

# Task 11: Python course students
for s in marks_data:
    if s["course"] == "Python":
        print(s["name"])

# Task 12: Course count
course_count = {}
for s in marks_data:
    course = s["course"]
    course_count[course] = course_count.get(course, 0) + 1
print(course_count)


# ================================
# PART 3 — CSV Handling
# ================================

import csv

# Task 13: Read attendance.csv
attendance = {}
with open("attendance.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        attendance[row["name"]] = row

# Task 14: Print attendance details
for name, data in attendance.items():
    print(name, data)

# Task 15: Attendance percentage
attendance_percent = {}
for name, data in attendance.items():
    percent = (int(data["days_present"]) / int(data["total_days"])) * 100
    attendance_percent[name] = percent
print(attendance_percent)

# Task 16: Below 80% attendance
for name, percent in attendance_percent.items():
    if percent < 80:
        print(name)

# Task 17: Best attendance
best = max(attendance_percent, key=attendance_percent.get)
print(best)


# ================================
# PART 4 — Data Structures Practice
# ================================

# Task 18: Marks summary
print(max(marks_list))
print(min(marks_list))
print(sum(marks_list))

# Task 19: Tuple of courses
courses_tuple = tuple([s["course"] for s in marks_data])
print(courses_tuple)

# Task 20: Unique courses set
courses_set = set(courses_tuple)
print(courses_set)

# Task 21: Name → Marks dictionary
marks_dict = {s["name"]: s["marks"] for s in marks_data}
print(marks_dict)

# Task 22: Name → Attendance dictionary
attendance_dict = {}
for name, percent in attendance.items():
    attendance_dict[name] = percent
print(attendance_dict)


# ================================
# PART 5 — Conditions and Loops
# ================================

# Task 23: Pass/Fail
for name, marks in marks_dict.items():
    if marks >= 50:
        print(name, "Pass")
    else:
        print(name, "Fail")

# Task 24: Grades
for name, marks in marks_dict.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(name, grade)

# Task 25: High performers
for name in marks_dict:
    if marks_dict[name] > 80 and attendance_percent[name] > 85:
        print(name)


# ================================
# PART 6 — Functions
# ================================

# Task 26: Read students
def read_students(file):
    with open(file, "r") as f:
        return [line.strip() for line in f]

students = read_students("students.txt")
print(students)

# Task 27: Load marks
def load_marks(file):
    import json
    with open(file) as f:
        return json.load(f)["students"]

marks_data = load_marks("marks.json")
print(marks_data)

# Task 28: Load attendance
def load_attendance(file):
    import csv
    result = {}
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            percent = (int(row["days_present"]) / int(row["total_days"])) * 100
            result[row["name"]] = percent
    return result

attendance = load_attendance("attendance.csv")
print(attendance)

# Task 29: Average marks function
def avg_marks(marks_list):
    return sum(marks_list) / len(marks_list)

marks_list = [s["marks"] for s in marks_data]
avg = avg_marks(marks_list)
print(avg)

# Task 30: Attendance % function
def attendance_percent_func(present, total):
    return (present / total) * 100

percent = attendance_percent_func(22, 25)
print(percent)

# Task 31: Topper function
def topper_func(data):
    return max(data, key=lambda x: x["marks"])

top = topper_func(marks_data)
print(top)

# Task 32: Grade function
def generate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"


# ================================
# PART 7 — Final Combined Analysis
# ================================

# Task 33: Combine data
final_data = {}
for s in marks_data:
    name = s["name"]
    final_data[name] = {
        "marks": s["marks"],
        "attendance": attendance[name],
        "course": s["course"],
        "grade": generate_grade(s["marks"])
    }

# Task 34: Print combined data
for name, data in final_data.items():
    print(name, data)

# Task 35: Eligible students
eligible = []
for name, data in final_data.items():
    if data["marks"] >= 75 and data["attendance"] >= 80:
        eligible.append(name)

print(eligible)

# Task 36: Students needing improvement
improve = []
for name, data in final_data.items():
    if data["marks"] < 75 or data["attendance"] < 80:
        improve.append(name)

print(improve)


# ================================
# PART 8 — Output File Generation
# ================================

# Task 37: Write report
with open("report.txt", "w") as f:
    f.write("Student Report\n")
    for name, data in final_data.items():
        f.write(
            f"{name} - Marks: {data['marks']} - Attendance: {round(data['attendance'],1)}% - Grade: {data['grade']}\n"
        )

# Task 39: Final summary output
print("Topper:", topper["name"])
print("Best Attendance:", best)
print("Average Marks:", round(avg, 1))
print("Eligible Students:", ", ".join(eligible))
print("Students Needing Improvement:", ", ".join(improve))


# ================================
# Task 40 — Main Function (Modular)
# ================================

def main():
    marks_data = load_marks("marks.json")
    attendance_percent = load_attendance("attendance.csv")

    final_data = {}
    for s in marks_data:
        name = s["name"]
        final_data[name] = {
            "marks": s["marks"],
            "attendance": attendance_percent[name],
            "course": s["course"],
            "grade": generate_grade(s["marks"])
        }

    marks_list = [s["marks"] for s in marks_data]
    avg = avg_marks(marks_list)

    top = topper_func(marks_data)["name"]
    best = max(attendance_percent, key=attendance_percent.get)

    eligible = []
    for name, data in final_data.items():
        if data["marks"] >= 75 and data["attendance"] >= 80:
            eligible.append(name)

    improve = []
    for name, data in final_data.items():
        if data["marks"] < 75 or data["attendance"] < 80:
            improve.append(name)

    with open("report.txt", "w") as f:
        f.write("Student Report\n")
        for name, data in final_data.items():
            f.write(
                f"{name} - Marks: {data['marks']} - Attendance: {round(data['attendance'],1)}% - Grade: {data['grade']}\n"
            )

    print("Topper:", top)
    print("Best Attendance:", best)
    print("Average Marks:", round(avg, 1))
    print("Eligible Students:", ", ".join(eligible))
    print("Students Needing Improvement:", ", ".join(improve))


main()