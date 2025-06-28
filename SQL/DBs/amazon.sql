-- Simplified SQL Schema with 7 records in each table
DROP DATABASE IF EXISTS `amazon`;
CREATE DATABASE `amazon`;
USE `amazon`;
-- Order Items Table (Many-to-Many Relationship)

-- Drop existing tables to avoid conflicts
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Customers Table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'Diana'),
(5, 'Ethan'),
(6, 'Fiona'),
(7, 'George');

-- Orders Table
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(101, 1, '2023-01-01'),
(102, 1, '2023-01-10'),
(103, 2, '2023-02-05'),
(104, 3, '2023-02-20'),
(105, 5, '2023-03-01'),
(106, 6, '2023-03-15'),
(107, 7, '2023-03-25');

-- Products Table
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(50),
  price DECIMAL(5,2)
);

INSERT INTO products VALUES
(1, 'Pen', 1.50),
(2, 'Notebook', 2.75),
(3, 'Backpack', 15.00),
(4, 'Pencil', 0.99),
(5, 'Eraser', 0.50),
(6, 'Marker', 1.80),
(7, 'Stapler', 3.99);



CREATE TABLE order_items (
  order_id INT,
  product_id INT,
  quantity INT,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items VALUES
(101, 1, 2),
(101, 2, 1),
(102, 3, 1),
(103, 1, 5),
(104, 4, 3),
(105, 5, 2),
(106, 6, 1);
