SELECT first_name as firstname, last_name as lastname from employees;

SELECT DISTINCT department_id from employees;

SELECT * from employees ORDER BY first_name DESC;

SELECT first_name, last_name, salary from employees;


SELECT employee_id, first_name, last_name, salary from employees ORDER BY salary ASC;

SELECT sum(salary) from employees; 

SELECT max(salary), min(salary) from employees;

SELECT avg(salary) from employees;

SELECT count(first_name) from employees;

SELECT UPPER(first_name) from employees;

SELECT SUBSTR(first_name,1,3) from employees;

SELECT first_name, last_name from employees;

SELECT first_name, last_name, LENGTH(CONCAT(first_name,last_name)) from employees;

SELECT * FROM employees WHERE  first_name ~ '[0-9]';

SELECT * from employees LIMIT 10;

SELECT first_name, last_name, salary from employees WHERE salary > 10000 and salary < 15000;

SELECT first_name, last_name, hire_date from employees WHERE  hire_date >= '1987-01-01' and hire_date < '1988-01-01';


SELECT first_name from employees WHERE first_name LIKE '%c%' and first_name LIKE '%e%';

SELECT employees.last_name, jobs.job_title, employees.salary
FROM employees 
INNER JOIN jobs on employees.job_id = jobs.job_id
WHERE jobs.job_title NOT LIKE '%Programmer%' and jobs.job_title NOT LIKE '%Shipping Clerk%' 
and employees.salary != '4500' and  employees.salary != '10000' and  employees.salary != '15000';
 
SELECT * from jobs;

SELECT first_name, last_name from employees WHERE last_name LIKE '______';

SELECT last_name from employees WHERE last_name LIKE '__e%'

SELECT employees.first_name, employees.last_name, jobs.job_title
FROM employees
INNER JOIN jobs ON jobs.job_id = employees.job_id;

SELECT * from employees WHERE last_name LIKE 'Jones' or last_name LIKE 'Blake' or last_name LIKE 'Scott' or last_name LIKE 'King' or last_name LIKE 'Ford';


