import csv

salary_details = dict()
dept_details = dict()
it_dept = []

with open("employees.csv",'r') as file:
    reader=csv.DictReader(file)

    for row in reader:
        names=row["name"]
        dept=row["department"]
        salary=int(row["salary"])
        salary_details[names]=salary
        dept_details[dept]=dept_details.get(dept,0)+1
        if dept=="IT":
            it_dept.append(names)

print("Employee names",salary_details.keys())
print("Employees working in IT",it_dept)
print("Average salary",sum(salary_details.values())/len(salary_details))
print("Highest Salary",max(salary_details,key=salary_details.get),salary_details[max(salary_details,key=salary_details.get)])
print("Count of employees per department:",dept_details)
