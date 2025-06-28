-- Create the employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert sample employee data
INSERT INTO employees (emp_id, name, age, department, salary) VALUES
(1, 'Hannah Johnson', 46, 'Marketing', 31029),
(2, 'Charlie Johnson', 33, 'Operations', 52122),
(3, 'Charlie Jones', 39, 'HR', 76478),
(4, 'Ian Garcia', 43, 'Operations', 56360),
(5, 'Charlie Garcia', 55, 'Marketing', 77277),
(6, 'David Smith', 41, 'Finance', 41151),
(7, 'Alice Johnson', 44, 'IT', 78867),
(8, 'Eva Williams', 34, 'HR', 70010),
(9, 'Ian Jones', 39, 'HR', 31145),
(10, 'Eva Davis', 49, 'Finance', 64191),
(11, 'Grace Smith', 28, 'HR', 68739),
(12, 'Frank Anderson', 25, 'Finance', 33392),
(13, 'Charlie Taylor', 53, 'IT', 50927),
(14, 'David Garcia', 33, 'Operations', 73097),
(15, 'Charlie Smith', 34, 'Operations', 51366),
(16, 'Bob Garcia', 55, 'Marketing', 57365),
(17, 'Eva Taylor', 59, 'IT', 52986),
(18, 'Alice Davis', 60, 'Finance', 56933),
(19, 'Charlie Davis', 31, 'Marketing', 53144),
(20, 'Charlie Anderson', 42, 'Finance', 40431);
