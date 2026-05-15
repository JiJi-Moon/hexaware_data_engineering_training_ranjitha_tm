create database inventory_management;
use inventory_management;

create table suppliers (
supplier_id int primary key auto_increment,
supplier_name varchar(100),
contact_email varchar(100)
);

create table products (
product_id int primary key auto_increment,
product_name varchar(100),
supplier_id int,
reorder_level int,
foreign key (supplier_id) references suppliers(supplier_id)
);

create table warehouses (
warehouse_id int primary key auto_increment,
warehouse_name varchar(100),
location varchar(100)
);

create table stock_movements (
movement_id int primary key auto_increment,
product_id int,
warehouse_id int,
quantity int,
movement_type varchar(20), -- IN / OUT
movement_date date,
foreign key (product_id) references products(product_id),
foreign key (warehouse_id) references warehouses(warehouse_id)
);

insert into suppliers (supplier_name, contact_email) values
('ABC Suppliers', 'abc@gmail.com'),
('Global Traders', 'global@gmail.com'),
('Fresh Supply Co', 'fresh@gmail.com');

select * from suppliers;

insert into products (product_name, supplier_id, reorder_level) values
('Laptop', 1, 10),
('Mouse', 1, 20),
('Keyboard', 2, 15),
('Monitor', 2, 8),
('Printer', 3, 5);

select * from products;

insert into warehouses (warehouse_name, location) values
('Main Warehouse', 'Chennai'),
('Backup Warehouse', 'Bangalore');

select * from warehouses;

insert into stock_movements (product_id, warehouse_id, quantity, movement_type, movement_date) values
(1, 1, 50, 'IN', '2026-01-10'),
(2, 1, 30, 'IN', '2026-01-12'),
(3, 2, 20, 'IN', '2026-01-15'),
(1, 1, 10, 'OUT', '2026-01-18'),
(2, 1, 5, 'OUT', '2026-01-20'),
(4, 2, 15, 'IN', '2026-01-22'),
(5, 2, 3, 'IN', '2026-01-25');

select * from stock_movements;

insert into products (product_name, supplier_id, reorder_level)
values ('Tablet', 1, 12);

select * from products
where product_name = 'Laptop';

update products
set reorder_level = 15
where product_id = 1;

insert into stock_movements (product_id, warehouse_id, quantity, movement_type, movement_date)
values (1, 1, 20, 'IN', curdate());

insert into stock_movements (product_id, warehouse_id, quantity, movement_type, movement_date)
values (1, 1, 5, 'OUT', curdate());

select 
p.product_name,
sum(case 
    when movement_type = 'IN' then quantity
    when movement_type = 'OUT' then -quantity
end) as current_stock
from stock_movements sm
join products p on sm.product_id = p.product_id
group by p.product_name;

select 
p.product_name,
sum(case 
    when movement_type = 'IN' then quantity
    when movement_type = 'OUT' then -quantity
end) as current_stock,
p.reorder_level
from stock_movements sm
join products p on sm.product_id = p.product_id
group by p.product_name, p.reorder_level
having current_stock < p.reorder_level;


select 
p.product_name,
sum(case 
    when movement_type = 'IN' then quantity
    when movement_type = 'OUT' then -quantity
end) as total_stock
from stock_movements sm
join products p on sm.product_id = p.product_id
group by p.product_name
order by total_stock desc
limit 1;

-- STORED PROCEDURE

delimiter $$

create procedure get_low_stock_products()
begin
    select 
        p.product_name,
        sum(case 
            when sm.movement_type = 'IN' then sm.quantity
            when sm.movement_type = 'OUT' then -sm.quantity
        end) as current_stock,
        p.reorder_level
    from products p
    join stock_movements sm on p.product_id = sm.product_id
    group by p.product_name, p.reorder_level
    having current_stock < p.reorder_level;
end $$

delimiter ;

call get_low_stock_products();