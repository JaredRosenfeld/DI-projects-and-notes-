UPDATE employees
SET email = 'not available'
WHERE department_id = 110;

UPDATE employees 
SET email = 'available'
WHERE department_id = (
	SELECT department_id 
	FROM departments 
	WHERE department_name = 'Accounting');


UPDATE employees 
SET salary = 8000 
WHERE employee_id = 105 AND salary < 5000; 

SELECT count(job_id) FROM employees; 

select department_name, count(employees.department_id) 
from departments
INNER JOIN employees on employees.department_id = departments.department_id
GROUP BY department_name;

select (max(max_salary) - min(min_salary)) from jobs;

SELECT employees.manager_id, min(employees.salary) from employees group by employees.manager_id; 

SELECT  jobs.job_title, avg(employees.salary)
FROM employees
INNER JOIN jobs ON jobs.job_id = employees.job_id 
WHERE jobs.job_title NOT LIKE 'Programmer'
GROUP BY jobs.job_title;

SELECT department_id, AVG(salary), COUNT(*) 
FROM employees 
GROUP BY department_id
HAVING COUNT(*) > 5;

ALTER TABLE locations
RENAME COLUMN state_province TO state;

ALTER TABLE locations 
ADD PRIMARY KEY (location_id);

CREATE TABLE new_countries(id SERIAL,country_name text CHECK (country_name in ('Italy','India','China')), PRIMARY KEY(id));

SELECT * from new_countries;

CREATE TABLE new_countries1 AS SELECT * from new_countries;

CREATE TABLE new_jobs(id SERIAL, job_title text, min_salary int DEFAULT 8000,max_salary int CHECK(max_salary <25000)DEFAULT NULL, PRIMARY KEY(id));

SELECT * from new_jobs;

CREATE TABLE new_employees(employee_id SERIAL UNIQUE,first_name text, last_name text, email varchar(55), 
						   phone_number varchar(15),hire_date date, job_id int,salary int, 
						   PRIMARY KEY (employee_id),
						   FOREIGN KEY (job_id) REFERENCES new_jobs(id) ON UPDATE CASCADE);

CREATE TABLE new_job_history(employee_id int, start_date date, end_date date, job_id int, FOREIGN KEY (employee_id) REFERENCES new_employees(employee_id),
							FOREIGN KEY(job_id) REFERENCES new_jobs(id) ON UPDATE CASCADE);

INSERT INTO new_countries(country_name)VALUES('China');
INSERT INTO new_countries(country_name)VALUES('China'),('India'),('Italy');

SELECT * INTO new_countries1 FROM new_countries;
UPDATE new_countries1
SET id = new_countries.id, country_name = new_countries.country_name
FROM new_countries; 

INSERT INTO new_countries1 SELECT * FROM new_countries;
SELECT * fROM new_countries1;

INSERT INTO new_jobs(job_title,min_salary,max_salary)VALUES('Marketing',8000,23000),('HR',8000,12000),('CEO',20000,24999);
INSERT INTO new_employees(first_name,last_name,email,phone_number,hire_date,job_id,salary)
VALUES('Bob','Peterson','bpson@gmail.com','(201)-661-3676','2021-05-12',1,'13000'),('Jared','Rosenfeld','jared@gmail.com','058-783-1516','2015-01-01',3,'23000');

SELECT * 
from new_employees
INNER JOIN new_jobs ON new_jobs.id = new_employees.job_id;
