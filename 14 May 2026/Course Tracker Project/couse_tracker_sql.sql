create database course_tracker;
use course_tracker;

create table students (
s_id int primary key auto_increment,
name varchar(50),
email varchar(100));

create table courses(
course_id int primary key auto_increment,
course_name varchar(50),
course_instructor varchar(50),
duration int);

create table enrollments(
enrollment_id int primary key auto_increment,
course_id int,
student_id int,
enrollement_date date,
foreign key(student_id) references students(s_id),
foreign key(course_id) references courses(course_id));

create table progress(
progress_id int primary key auto_increment,
enrollment_id int,
course_progress float,
updated_date date,
foreign key(enrollment_id) references enrollments(enrollment_id));

insert into students (name,email) values
('Ranjitha', 'ranjitha@gmail.com'),
('Arun', 'arun@gmail.com'),
('Meena', 'meena@gmail.com'),
('Karthik', 'karthik@gmail.com'),
('Divya', 'divya@gmail.com');

select * from students;

insert into courses (course_name,course_instructor,duration) values
('Deep Learning', 'Dr. Kumar', 60),
('Data Science', 'Dr. Priya', 45),
('Cloud Computing', 'Mr. Ravi', 30),
('NLP', 'Dr. Anitha', 50),
('Big Data Analytics', 'Mr. Suresh', 40);

select * from courses;

insert into enrollments (course_id,student_id,enrollement_date) values
(1, 1, '2026-01-10'),
(2, 1, '2026-01-12'),
(3, 2, '2026-01-15'),
(1, 3, '2026-01-18'),
(4, 4, '2026-01-20'),
(5, 5, '2026-01-22'),
(2, 3, '2026-01-25');

select * from enrollments;

insert into progress (enrollment_id,course_progress,updated_date) values
(1, 40, '2026-02-01'),
(2, 75, '2026-02-05'),
(3, 20, '2026-02-03'),
(4, 90, '2026-02-10'),
(5, 60, '2026-02-12'),
(6, 30, '2026-02-15'),
(7, 50, '2026-02-18');

select * from progress;

select s.name,p.course_progress from progress p join enrollments e on e.enrollment_id=p.enrollment_id join students s on e.student_id=s.s_id;

INSERT INTO students (name, email)
VALUES ('Vikram', 'vikram@gmail.com');

insert into students (name, email)
values ('vikram', 'vikram@gmail.com');

select * from students
where name = 'ranjitha';

update students
set email = 'ranjitha_new@gmail.com'
where s_id = 1;

insert into courses (course_name, course_instructor, duration)
values ('machine learning', 'dr. raj', 55);

select course_name, duration
from courses
where duration > 40;

update courses
set duration = 65
where course_id = 1;

delete from courses
where course_id = 5;

insert into enrollments (course_id, student_id, enrollement_date)
values (3, 1, curdate());

select s.name, c.course_name, p.course_progress
from progress p
join enrollments e on p.enrollment_id = e.enrollment_id
join students s on e.student_id = s.s_id
join courses c on e.course_id = c.course_id
where p.course_progress < 50;

select c.course_name, avg(p.course_progress) as avg_progress
from progress p
join enrollments e on p.enrollment_id = e.enrollment_id
join courses c on e.course_id = c.course_id
group by c.course_name;

select c.course_name, count(*) as total_enrollments
from enrollments e
join courses c on e.course_id = c.course_id
group by c.course_name
order by total_enrollments desc
limit 1;

delimiter $$

create procedure get_completion_status(in sid int)
begin
    select 
        s.name,
        c.course_name,
        p.course_progress,
        case
            when p.course_progress >= 50 then 'completed'
            else 'in progress'
        end as status
    from students s
    join enrollments e on s.s_id = e.student_id
    join courses c on e.course_id = c.course_id
    join progress p on e.enrollment_id = p.enrollment_id
    where s.s_id = sid;
end $$

delimiter ;

call get_completion_status(1);
        
