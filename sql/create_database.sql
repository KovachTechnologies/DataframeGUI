-- Create the database
CREATE DATABASE IF NOT EXISTS SampleData;

-- Use the database
USE SampleData;

-- Create the table
CREATE TABLE IF NOT EXISTS records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME NOT NULL,
    name VARCHAR(255) NOT NULL,
    column1 DECIMAL(10, 2) NOT NULL,
    column2 DECIMAL(10, 2) NOT NULL
);

-- Insert sample data for testing
INSERT INTO records (date, name, column1, column2) VALUES
    ('2025-08-01 10:00:00', 'Alice', 100.50, 200.75),
    ('2025-08-02 12:30:00', 'Bob', 150.25, 300.10),
    ('2025-08-03 15:45:00', 'Charlie', 200.00, 400.50);
