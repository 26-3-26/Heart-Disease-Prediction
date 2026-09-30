create DATABASE my_practice_db;
use my_practice_db;

CREATE TABLE raw_customers (
    customer_id INT,
    full_name   VARCHAR(100),
    email       VARCHAR(100),
    signup_date DATE,
    total_spent DECIMAL(10, 2) 
);
     
USE my_practice_db;

INSERT INTO raw_customers (customer_id, full_name, email, signup_date, total_spent)
VALUES 
    (101, '  ALEX SMITH ', 'alex@gmail.com', '2026-01-15', 150.00),
    (101, 'alex smith',     'alex@gmail.com', '2026-01-15', 150.00),
    (102, 'SARA J.',        NULL,             '2026-02-01', NULL),
    (103, 'Omar Kh.',       'OMAR@YAHOO.COM', '2026-02-10', 85.50);

    select * from raw_customers;
    