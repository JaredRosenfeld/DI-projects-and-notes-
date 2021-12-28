-- SCHEMA: public

-- DROP SCHEMA public ;
1
SELECT name from language;



-- 2
SELECT film.title, film.description, language.name
FROM film
FULL OUTER JOIN language
ON film.language_id = language.language_id;

SELECT film.title, film.description, language.name
FROM film
RIGHT JOIN language
ON film.language_id = language.language_id;

3
CREATE TABLE new_film(id1 SERIAL UNIQUE, name text);
INSERT INTO new_film(name)VALUES('Red October');
INSERT INTO new_film(name)VALUES('Die Another Day');
INSERT INTO new_film(name)VALUES('Spartacus');
INSERT INTO new_film(name)VALUES('Platoon');

4
CREATE TABLE customer_review(review_id SERIAL, 
							 film_id INTEGER REFERENCES new_film (id1) ON DELETE CASCADE,
							 language_id INTEGER REFERENCES language(language_id),
							 title TEXT,
							 score smallint,
							 review_text TEXT,
							 last_update date) 
INSERT INTO customer_review(film_id, title, score,review_text,last_update)VALUES(1,'Platoon',10,'Best movie ever!', '2021/11/15');
SELECT * from customer_review;
INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update)VALUES(3,1,'Spartacus',10,'Best movie of the 60s!', '2021/11/15');
INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update)VALUES(1,1,'Red October',10,'A True classic', '2021/11/15');

DELETE FROM customer_review WHERE title = 'Platoon';
DELETE FROM new_film WHERE name  = 'Spartacus';
SELECT * from customer_review;

EX2
1
UPDATE film SET language_id = 6 WHERE film_id = 6;
SELECT * from film WHERE language_id = 6;
UPDATE film SET language_id = 6 WHERE film_id = 55;
UPDATE film SET language_id = 2 WHERE film_id = 64;
UPDATE film SET language_id = 6 WHERE film_id = 444;
2
customer ID 
3
DROP TABLE customer_review;
4
SELECT * from rental WHERE return_date is NULL;
5
SELECT rental.rental_id, rental.return_date, payment.amount 
from rental
INNER JOIN payment
ON rental.rental_id = payment.rental_id
WHERE return_date is NULL
ORDER BY payment.amount DESC LIMIT 30;
6
SELECT film.title
FROM film 
INNER JOIN film_actor ON film.film_id = film_actor.film_id 
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.description LIKE '%Sumo%';
SELECT film.title 
FROM film 
WHERE length < 60 AND rating = 'R';

SELECT film.title
FROM film 
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer ON rental.customer_id =  customer.customer_id
INNER JOIN payment ON payment.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND film.rental_rate >4 AND rental.return_date >='2005/07/28' AND rental.return_date <= '2005/08/01';

SELECT film.title
FROM film 
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer ON rental.customer_id =  customer.customer_id
INNER JOIN payment ON payment.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND (film.description LIKE '%Boat%' OR film.title LIKE '%Boat%') LIMIT 1;