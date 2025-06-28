DROP DATABASE IF EXISTS hr;
CREATE DATABASE hr;
USE hr;

-- Offices table
CREATE TABLE offices (
  id INT PRIMARY KEY,
  city VARCHAR(50),
  state VARCHAR(50)
);

INSERT INTO offices VALUES
(1, 'Cincinnati', 'OH'),
(2, 'New York City', 'NY'),
(3, 'Richmond', 'VA'),
(4, 'Minneapolis', 'MN'),
(5, 'Aurora', 'CO');

-- Employees table
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  title VARCHAR(50),
  salary INT,
  manager_id INT,
  office_id INT,
  FOREIGN KEY (manager_id) REFERENCES employees(id),
  FOREIGN KEY (office_id) REFERENCES offices(id)
);

INSERT INTO employees VALUES
(1, 'Alice', 'CEO', 150000, NULL, 1),
(2, 'Bob', 'Sales Rep', 62000, 1, 1),
(3, 'Charlie', 'Analyst', 58000, 1, 1),
(4, 'David', 'Professor', 53000, 1, 2),
(5, 'Eve', 'Assistant', 42000, 1, 2),
(6, 'Frank', 'Sys Analyst', 76000, 1, 3),
(7, 'Grace', 'Manager', 93000, 1, 3);
