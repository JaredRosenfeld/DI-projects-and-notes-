SCHEMA: public

DROP SCHEMA public ;

SELECT * from rental WHERE return_date is NULL;

SELECT customer.first_name, customer.last_name 
FROM customer
INNER JOIN rental
ON customer.customer_id = rental.customer_id
WHERE return_date is NULL;

SELECT film.title 
FROM film 
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'Joe' and actor.last_name = 'Swank';

SELECT count(store.store_id), country.country, city.city
FROM store
INNER JOIN address ON store.address_id = address.address_id 
FULL OUTER JOIN city ON address.city_id = city.city_id
FULL OUTER JOIN country ON city.country_id = country.country_id
GROUP BY country,city;

SELECT sum(film.length)
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN store ON inventory.store_id = store.store_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE rental.return_date IS NOT NULL
GROUP BY store;

SELECT customer.first_name, customer.last_name, city.city
FROM customer
INNER JOIN address ON customer.address_id = address.address_id 
FULL OUTER JOIN store ON address.address_id = store.address_id
INNER JOIN city ON address.city_id = city.city_id;

SELECT customer.first_name, customer.last_name, country.country
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
FULL OUTER JOIN store ON address.address_id = store.address_id
INNER JOIN city ON address.city_id = city.city_id
INNER JOIN country ON city.country_id = country.country_id;

CREATE TABLE safelist(id SERIAL, title text, description text);

SELECT film.title, film.description, sum(film.length), category.name
INTO safelist
FROM film
INNER JOIN film_category on film.film_id = film_category.film_id
FULL OUTER JOIN category on category.category_id = film_category.category_id
GROUP BY film.title, film.description, category.name;

DELETE FROM safelist WHERE name = 'Horror';


-- DELETE FROM safelist WHERE description LIKE '%beast%';
DELETE FROM safelist WHERE description LIKE '%monster%';
DELETE FROM safelist WHERE description LIKE '%ghost%';
DELETE FROM safelist WHERE description LIKE '%dead%';
DELETE FROM safelist WHERE description LIKE '%zombie%';
DELETE FROM safelist WHERE description LIKE '%undead%';

	

SELECT * from safelist;

ALTER TABLE safelist
add column hours smallint;

ALTER TABLE safelist
add column days smallint;

UPDATE safelist SET hours = (sum/60);

UPDATE safelist SET days = (hours/24);
SELECT * from safelist

