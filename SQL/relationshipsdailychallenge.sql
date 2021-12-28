-- Database: relationshipsexample

-- DROP DATABASE relationshipsexample;

-- CREATE DATABASE relationshipsexample
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_World.1252'
--     LC_CTYPE = 'English_World.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;


-- CREATE TABLE customer(id SERIAL, name text, age smallint, PRIMARY KEY(id));
-- INSERT INTO customer(name,age)VALUES('Jared',26);
-- CREATE TABLE customer_profile(ID SERIAL, address text, prefrences text, FOREIGN KEY (ID) REFERENCES  customer(id));
-- INSERT INTO customer_profile(address,prefrences)VALUES('Israel','minning');
-- SELECT * from customer_profile;

-- SELECT * 
-- from customer 
-- FULL OUTER JOIN customer_profile on customer_profile.id = customer.id;

-- SELECT customer.name, customer_profile.prefrences
-- from customer 
-- RIGHT OUTER JOIN customer_profile on customer_profile.id = customer.id;

-- CREATE TABLE product(id SERIAL, name text, price smallint, PRIMARY KEY(id));
-- INSERT INTO product(name,price)VALUES('2080 TI', 1000);
-- CREATE TABLE orders(id SERIAL, name text , price smallint, customer smallint, FOREIGN KEY (customer) REFERENCES customer(id))
-- INSERT INTO orders(name,price)VALUES('2080 TI', 1000);

SELECT * 
from customer 
FULL OUTER JOIN orders on orders.customer = customer.id
FULL OUTER JOIN product on product.id = orders.id
FULL OUTER JOIN customer_profile on customer_profile.id = customer.id;