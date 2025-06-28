DROP DATABASE IF EXISTS product;
CREATE DATABASE product;
USE product;


-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    discount DECIMAL(5, 2),
    description TEXT
);

-- Insert sample data into products table
INSERT INTO products (product_id, name, price, discount, description) VALUES
(1, 'Wireless Mouse', 66.57, 6.82, 'Wireless Mouse - High quality tech gadget'),
(2, 'Gaming Keyboard', 463.91, 16.37, 'Gaming Keyboard - High quality tech gadget'),
(3, 'USB-C Hub', 58.43, -3.56, 'USB-C Hub - High quality tech gadget'),
(4, 'Portable SSD', 219.80, -13.70, 'Portable SSD - High quality tech gadget'),
(5, 'Webcam', 188.87, 12.18, 'Webcam - High quality tech gadget'),
(6, 'Noise Cancelling Headphones', 92.26, 2.39, 'Noise Cancelling Headphones - High quality tech gadget'),
(7, 'Laptop Stand', 303.72, 9.58, 'Laptop Stand - High quality tech gadget'),
(8, 'Bluetooth Speaker', 284.00, 8.01, 'Bluetooth Speaker - High quality tech gadget'),
(9, 'Smartwatch', 57.05, -12.97, 'Smartwatch - High quality tech gadget'),
(10, 'Monitor Arm', 418.61, -19.95, 'Monitor Arm - High quality tech gadget'),
(11, 'Webcam HD', 109.25, 5.30, 'Webcam HD - Improved clarity and zoom'),
(12, 'Gaming Mouse', 75.80, 10.00, 'Gaming Mouse - Ergonomic and precise'),
(13, 'Tablet Stand', 55.95, -5.55, 'Tablet Stand - Adjustable angle support'),
(14, 'USB Power Strip', 65.40, 0.00, 'USB Power Strip - 6 ports fast charging'),
(15, 'Laptop Cooling Pad', 85.99, 7.25, 'Laptop Cooling Pad - Quiet and efficient'),
(16, 'HDMI Switch', 49.99, -2.50, 'HDMI Switch - 3 in 1 out with remote'),
(17, 'Desk Lamp', 59.90, 4.80, 'Desk Lamp - LED dimmable with USB'),
(18, 'Ergonomic Chair', 389.00, 15.50, 'Ergonomic Chair - Mesh back and lumbar support'),
(19, 'Standing Desk', 499.99, -10.00, 'Standing Desk - Adjustable electric frame'),
(20, 'Wireless Charger', 64.49, 6.00, 'Wireless Charger - Fast charging compatible');
