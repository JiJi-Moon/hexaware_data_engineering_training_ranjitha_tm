CREATE DATABASE company_training;
USE company_training;

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
city VARCHAR(50)
);

CREATE TABLE projects (
project_id INT PRIMARY KEY,
emp_id INT,
project_name VARCHAR(100),
project_budget DECIMAL(12,2),
project_status VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', NULL),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, NULL, 'Marketing', 'Chennai');

INSERT INTO projects VALUES
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, NULL, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');


-- Basic Join 

select employees.emp_name, projects.project_name,projects.project_budget
from employees inner join projects on employees.emp_id=projects.emp_id; 

select * from employees left join projects on employees.emp_id=projects.emp_id;

select * from employees right join projects on employees.emp_id=projects.emp_id;

select * from employees full outer join projects on employees.emp_id=projects.emp_id;

select * from employees left join projects on employees.emp_id=projects.emp_id
union
select * from employees right join projects on employees.emp_id=projects.emp_id;

select * from employees cross join projects;

-- join with filtering 
select p.project_name  from employees e inner join projects p on e.emp_id=p.emp_id where e.department='IT';

select p.project_name,p.project_id from employees e inner join projects p on e.emp_id=p.emp_id where p.project_budget>100000;

select e.emp_name,p.project_name from employees e inner join projects p on e.emp_id=p.emp_id where e.city='Hyderabad';

-- join with Aggregate Functions 

select e.emp_name, count(*) from employees e left join projects p on e.emp_id=p.emp_id group by e.emp_id;

select e.emp_name, sum(p.project_budget) from employees e inner join projects p on e.emp_id=p.emp_id group by e.emp_id;

select e.department, avg(p.project_budget) from employees e inner join projects p on e.emp_id=p.emp_id group by e.department;

-- Group By 

select e.department, count(*) from employees e left join projects p on e.emp_id=p.emp_id group by e.department;

select e.emp_name, sum(p.project_budget) as TotalBudget from employees e left join projects p on e.emp_id=p.emp_id group by e.emp_id;

select city,count(*) as NumberOfEmployees from employees group by city;

-- Having 

select e.emp_name, count(*) as Count from employees e inner join projects p on e.emp_id=p.emp_id group by e.emp_id having count(*)>1;

select e.department, sum(p.project_budget) as TotalBudget from employees e inner join projects p on e.emp_id=p.emp_id group by department having sum(project_budget)>150000;

select e.emp_name, sum(p.project_budget) as TotalBudget from employees e inner join projects p on e.emp_id=p.emp_id group by e.emp_id having sum(project_budget)>100000;

-- Capestone Query 

select e.emp_name as EmployeeName, e.department, sum(p.project_budget) as TotalProjectBudget 
from employees e inner join projects p on e.emp_id=p.emp_id
group by e.emp_id 
having sum(p.project_budget)>100000 
order by TotalProjectBudget desc;






