-- Drop tables if they already exist (for clean testing)
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Address;

-- Create Person table
CREATE TABLE Person (
    personId INT PRIMARY KEY,
    lastName VARCHAR(50),
    firstName VARCHAR(50)
);

-- Create Address table
CREATE TABLE Address (
    addressId INT PRIMARY KEY,
    personId INT,
    city VARCHAR(50),
    state VARCHAR(50)
);

-- Insert test data into Person
INSERT INTO Person (personId, lastName, firstName) VALUES
(1, 'Wang', 'Allen'),    -- has no address
(2, 'Alice', 'Bob'),     -- has address
(3, 'Kumar', 'Ravi');    -- has address

-- Insert test data into Address
INSERT INTO Address (addressId, personId, city, state) VALUES
(1, 2, 'New York City', 'USA'),
(2, 3, 'Delhi', 'India'),
(3, 99, 'Paris', 'France'); -- extra address (no matching person)

-- Query: LEFT JOIN so all persons appear, NULL if no address
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;