create table items(
item_id serial primary key,
title varchar (255) not null,
price int,
last_update timestamp
);
create table orders (
order_id int not null,
item_id int not null,
quantity int not null,
last_update timestamp,
foreign key (item_id) references items(item_id) on delete cascade);


insert into items(title, price, last_update)values ('TV', 82, '2021-11-11');
insert into items(title, price, last_update)values ('Flat Screen TV', 110, '2021-11-07')
insert into orders(order_id, item_id, quantity)values (1, 1, 1);
insert into orders(order_id, item_id, quantity)values (1, 2, 3);



create table users(
id serial primary key,
first_name varchar(255),
last_name varchar(255)
);

alter table orders add column user_id int;

alter table orders add foreign key (user_id) references users(id);

update orders set user_id = 3 where order_id = 3;

insert into users(first_name, last_name)values ('Bob', 'Ross'), ('Michael', 'Smith'), ('Jennifer', 'Lopez');

select sum (price * quantity)
from orders inner join items on orders.item_id = items.item_id;

insert into orders(order_id, item_id, quantity,user_id)values (1, 2, 2,2);

select sum (items.price * orders.quantity),users.first_name, users.last_name
from orders inner join items on orders.item_id = items.item_id
INNER JOIN users on users.id = orders.user_id
GROUP BY users.first_name, users.last_name;


select * from total_price(1, ‘Bob’);
