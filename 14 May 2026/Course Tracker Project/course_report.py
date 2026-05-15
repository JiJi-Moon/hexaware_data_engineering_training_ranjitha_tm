import csv
import pandas as pd
import numpy as np

students_data = [
    ['student_id', 'name', 'email'],
    [1, 'ranjitha', 'ranjitha@gmail.com'],
    [2, 'arun', 'arun@gmail.com'],
    [3, 'meena', 'meena@gmail.com'],
    [4, 'karthik', 'karthik@gmail.com'],
    [5, 'divya', 'divya@gmail.com']
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

courses_data = [
    ['course_id', 'course_name', 'instructor'],
    [1, 'deep learning', 'dr. kumar'],
    [2, 'data science', 'dr. priya'],
    [3, 'cloud computing', 'mr. ravi'],
    [4, 'nlp', 'dr. anitha'],
    [5, 'big data', 'mr. suresh']
]

with open('courses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(courses_data)

enrollments_data = [
    ['enrollment_id', 'student_id', 'course_id', 'enrollment_date'],
    [1, 1, 1, '2026-01-10'],
    [2, 1, 2, '2026-01-12'],
    [3, 2, 3, '2026-01-15'],
    [4, 3, 1, '2026-01-18'],
    [5, 4, 4, '2026-01-20'],
    [6, 5, 5, '2026-01-22'],
    [7, 3, 2, '2026-01-25']
]

with open('enrollments.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(enrollments_data)

progress_data = [
    ['progress_id', 'enrollment_id', 'completion_percentage', 'last_updated'],
    [1, 1, 40, '2026-02-01'],
    [2, 2, 75, '2026-02-05'],
    [3, 3, 20, '2026-02-03'],
    [4, 4, 90, '2026-02-10'],
    [5, 5, '', '2026-02-12'],
    [6, 6, 120, '2026-02-15'],
    [7, 7, -10, '2026-02-18']
]

with open('progress.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(progress_data)


students = pd.read_csv("students.csv")
courses = pd.read_csv("courses.csv")
enrollments = pd.read_csv("enrollments.csv")
progress = pd.read_csv("progress.csv")


data = enrollments.merge(progress, on="enrollment_id") .merge(students, on="student_id").merge(courses, on="course_id")

print("raw data:\n", data)

data['completion_percentage'] = data['completion_percentage'].fillna(0)

data['completion_percentage'] = np.clip(data['completion_percentage'], 0, 100)

data = data.dropna(subset=['name', 'enrollment_date'])

print("\ncleaned data:\n", data)

avg_progress = np.mean(data['completion_percentage'])
print("\naverage progress:", avg_progress)

course_summary = data.groupby('course_name')['completion_percentage'].mean()
print("\ncourse-wise average:\n", course_summary)

low_progress = data[data['completion_percentage'] < 50]
print("\nlow progress students:\n",
      low_progress[['name', 'course_name', 'completion_percentage']])

data.to_csv("cleaned_progress.csv", index=False)
course_summary.to_csv("course_summary.csv")
