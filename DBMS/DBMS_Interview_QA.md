# DBMS Interview Q&A - Complete Guide

## Interview Preparation Guide for Campus Placement
**Dayanand Sagar Engineering - 4th Year**

---

## 📑 Table of Contents

**Legend:** 🟢 Easy | 🟡 Medium | 🔴 Hard | ⏱️ Estimated Time

### BASIC LEVEL (Q1-Q15) ⏱️ 60-75 min
1. [🟢 What is DBMS?](#q1-what-is-dbms) ⏱️ 4 min
2. [🟢 Database vs DBMS vs RDBMS](#q2-database-vs-dbms-vs-rdbms) ⏱️ 5 min
3. [🟢 What is SQL?](#q3-what-is-sql) ⏱️ 4 min
4. [🟢 Types of SQL Commands](#q4-types-of-sql-commands) ⏱️ 5 min
5. [🟢 Primary Key vs Foreign Key](#q5-primary-key-vs-foreign-key) ⏱️ 5 min
6. [🟢 What is Normalization?](#q6-what-is-normalization) ⏱️ 5 min
7. [🟢 Normal Forms (1NF, 2NF, 3NF)](#q7-normal-forms-1nf-2nf-3nf) ⏱️ 6 min
8. [🟢 What are Constraints?](#q8-what-are-constraints) ⏱️ 5 min
9. [🟢 ACID Properties](#q9-acid-properties) ⏱️ 5 min
10. [🟢 What is a Transaction?](#q10-what-is-a-transaction) ⏱️ 4 min
11. [🟢 SELECT, WHERE, ORDER BY](#q11-select-where-order-by) ⏱️ 5 min
12. [🟢 Aggregate Functions](#q12-aggregate-functions) ⏱️ 5 min
13. [🟢 GROUP BY vs HAVING](#q13-group-by-vs-having) ⏱️ 5 min
14. [🟢 What are Indexes?](#q14-what-are-indexes) ⏱️ 4 min
15. [🟢 DELETE vs TRUNCATE vs DROP](#q15-delete-vs-truncate-vs-drop) ⏱️ 5 min

### INTERMEDIATE LEVEL (Q16-Q35) ⏱️ 90-110 min
16. [🟡 Types of Joins](#q16-types-of-joins) ⏱️ 6 min
17. [🟡 INNER vs OUTER JOIN](#q17-inner-vs-outer-join) ⏱️ 5 min
18. [🟡 Self Join and Cross Join](#q18-self-join-and-cross-join) ⏱️ 5 min
19. [🟡 Subqueries and Nested Queries](#q19-subqueries-and-nested-queries) ⏱️ 6 min
20. [🟡 Views in SQL](#q20-views-in-sql) ⏱️ 5 min
21. [🟡 Stored Procedures](#q21-stored-procedures) ⏱️ 5 min
22. [🟡 Triggers](#q22-triggers) ⏱️ 5 min
23. [🟡 Cursor in SQL](#q23-cursor-in-sql) ⏱️ 5 min
24. [🟡 BCNF (Boyce-Codd Normal Form)](#q24-bcnf-boyce-codd-normal-form) ⏱️ 6 min
25. [🟡 Functional Dependency](#q25-functional-dependency) ⏱️ 5 min
26. [🟡 Entity-Relationship Model](#q26-entity-relationship-model) ⏱️ 6 min
27. [🟡 Cardinality in DBMS](#q27-cardinality-in-dbms) ⏱️ 5 min
28. [🟡 Clustered vs Non-Clustered Index](#q28-clustered-vs-non-clustered-index) ⏱️ 5 min
29. [🟡 B-Tree and B+ Tree](#q29-b-tree-and-b-tree) ⏱️ 6 min
30. [🟡 Locking Mechanisms](#q30-locking-mechanisms) ⏱️ 5 min
31. [🟡 Deadlock](#q31-deadlock) ⏱️ 5 min
32. [🟡 UNION vs UNION ALL](#q32-union-vs-union-all) ⏱️ 4 min
33. [🟡 Window Functions](#q33-window-functions) ⏱️ 6 min
34. [🟡 CTE (Common Table Expression)](#q34-cte-common-table-expression) ⏱️ 5 min
35. [🟡 Data Warehousing Basics](#q35-data-warehousing-basics) ⏱️ 5 min

### ADVANCED LEVEL (Q36-Q50) ⏱️ 75-90 min
36. [🔴 Query Optimization Techniques](#q36-query-optimization-techniques) ⏱️ 6 min
37. [🔴 CAP Theorem](#q37-cap-theorem) ⏱️ 5 min
38. [🔴 NoSQL vs SQL](#q38-nosql-vs-sql) ⏱️ 6 min
39. [🔴 Sharding and Partitioning](#q39-sharding-and-partitioning) ⏱️ 6 min
40. [🔴 Replication](#q40-replication) ⏱️ 5 min
41. [🔴 Two-Phase Commit](#q41-two-phase-commit) ⏱️ 6 min
42. [🔴 Serializability](#q42-serializability) ⏱️ 6 min
43. [🔴 Phantom Read, Dirty Read](#q43-phantom-read-dirty-read) ⏱️ 5 min
44. [🔴 Isolation Levels](#q44-isolation-levels) ⏱️ 6 min
45. [🔴 Database Design Best Practices](#q45-database-design-best-practices) ⏱️ 5 min
46. [🔴 OLTP vs OLAP](#q46-oltp-vs-olap) ⏱️ 5 min
47. [🔴 Star Schema vs Snowflake Schema](#q47-star-schema-vs-snowflake-schema) ⏱️ 5 min
48. [🔴 Horizontal vs Vertical Scaling](#q48-horizontal-vs-vertical-scaling) ⏱️ 4 min
49. [🔴 Multi-Version Concurrency Control (MVCC)](#q49-multi-version-concurrency-control-mvcc) ⏱️ 6 min
50. [🔴 Database Backup and Recovery](#q50-database-backup-and-recovery) ⏱️ 5 min

### Quick Reference Sections
- [📊 Key Comparison Tables](#-key-comparison-tables)
- [🎯 Top 10 Most Asked Questions](#-top-10-most-asked-questions)
- [📝 SQL Syntax Cheat Sheet](#-sql-syntax-cheat-sheet)
- [💡 Interview Tips](#-interview-tips)

---

## BASIC LEVEL QUESTIONS

### Q1. What is DBMS? 🟢

**Definition:**
DBMS (Database Management System) is software that manages and organizes data in a structured way. It provides an interface for users to create, read, update, and delete data while ensuring data integrity, security, and concurrent access.

**Why it matters:**
Understanding DBMS fundamentals is essential as it forms the foundation of data management in modern applications. Every company uses databases to store critical business information.

**Real-World Example:**
```sql
-- Creating a database for a library management system
CREATE DATABASE LibraryDB;

USE LibraryDB;

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50),
    published_year INT
);
```

**Key Advantages:**
- **Data Independence**: Application programs don't need to know data storage details
- **Data Sharing**: Multiple users can access data simultaneously
- **Data Security**: Access controls and authentication
- **Reduced Redundancy**: Avoid duplicate data storage

**Key Takeaway:**
DBMS provides structured, secure, and efficient data management with features like ACID properties, concurrent access, and data independence.

---

### Q2. Database vs DBMS vs RDBMS 🟢

**Definition:**
- **Database**: Collection of organized data
- **DBMS**: Software to manage databases
- **RDBMS**: DBMS that stores data in tables with relationships

**Why it matters:**
Knowing the distinction helps in choosing the right technology stack and communicating effectively about database systems.

**Comparison Table:**

| Aspect | Database | DBMS | RDBMS |
|--------|----------|------|-------|
| **What is it?** | Data collection | Management software | Relational management software |
| **Structure** | Any format | Files/tables | Tables with relationships |
| **Examples** | Excel file, text file | File system, MongoDB | MySQL, PostgreSQL, Oracle |
| **Relationships** | May not have | Limited | Strong relationships via foreign keys |
| **ACID** | No | Partial | Full ACID compliance |

**Code Example:**
```sql
-- RDBMS example showing relationships
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
```

**Key Takeaway:**
RDBMS is a specialized DBMS that enforces relationships between tables using keys and maintains data integrity.

---

### Q3. What is SQL? 🟢

**Definition:**
SQL (Structured Query Language) is a standard programming language used to communicate with relational databases. It allows you to create, manipulate, and query data stored in RDBMS.

**Why it matters:**
SQL is the universal language for interacting with databases. Mastering SQL is critical for any role involving data.

**SQL Operations:**
```sql
-- CREATE: Create new database objects
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

-- INSERT: Add data
INSERT INTO Students VALUES (1, 'Alice', 20);

-- SELECT: Query data
SELECT * FROM Students WHERE age > 18;

-- UPDATE: Modify data
UPDATE Students SET age = 21 WHERE name = 'Alice';

-- DELETE: Remove data
DELETE FROM Students WHERE id = 1;
```

**Key Takeaway:**
SQL provides a declarative way to interact with databases - you specify what you want, not how to get it.

---

### Q4. Types of SQL Commands 🟢

**Definition:**
SQL commands are categorized into five types based on their functionality:

1. **DDL (Data Definition Language)**: Structure operations
2. **DML (Data Manipulation Language)**: Data operations
3. **DCL (Data Control Language)**: Permission operations
4. **TCL (Transaction Control Language)**: Transaction operations
5. **DQL (Data Query Language)**: Query operations

**Why it matters:**
Understanding command categories helps in database design, security, and transaction management.

**Command Categories:**

| Category | Commands | Purpose | Example |
|----------|----------|---------|---------|
| **DDL** | CREATE, ALTER, DROP, TRUNCATE | Define schema | `CREATE TABLE` |
| **DML** | INSERT, UPDATE, DELETE | Manipulate data | `INSERT INTO` |
| **DCL** | GRANT, REVOKE | Control access | `GRANT SELECT` |
| **TCL** | COMMIT, ROLLBACK, SAVEPOINT | Manage transactions | `COMMIT;` |
| **DQL** | SELECT | Query data | `SELECT * FROM` |

**Code Examples:**
```sql
-- DDL: Define structure
CREATE TABLE Employees (id INT, name VARCHAR(50));
ALTER TABLE Employees ADD salary DECIMAL(10,2);
DROP TABLE Employees;

-- DML: Manipulate data
INSERT INTO Employees VALUES (1, 'John', 50000);
UPDATE Employees SET salary = 55000 WHERE id = 1;
DELETE FROM Employees WHERE id = 1;

-- DCL: Control access
GRANT SELECT ON Employees TO user1;
REVOKE SELECT ON Employees FROM user1;

-- TCL: Manage transactions
BEGIN TRANSACTION;
UPDATE Accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- DQL: Query data
SELECT name, salary FROM Employees WHERE salary > 40000;
```

**Key Takeaway:**
SQL commands are organized by purpose - DDL for structure, DML for data, DCL for security, TCL for transactions, DQL for queries.

---

### Q5. Primary Key vs Foreign Key 🟢

**Definition:**
- **Primary Key**: Unique identifier for each record in a table (cannot be NULL)
- **Foreign Key**: Field in one table that references the primary key of another table

**Why it matters:**
Keys establish relationships between tables and maintain referential integrity, which is fundamental to relational database design.

**Comparison:**

| Aspect | Primary Key | Foreign Key |
|--------|-------------|-------------|
| **Purpose** | Uniquely identifies records | Creates relationships |
| **Uniqueness** | Must be unique | Can have duplicates |
| **NULL** | Cannot be NULL | Can be NULL |
| **Count** | One per table | Multiple allowed |
| **Example** | Employee_ID | Department_ID (references Departments) |

**Code Example:**
```sql
-- Primary Key example
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- Foreign Key example
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Insert data
INSERT INTO Departments VALUES (1, 'IT'), (2, 'HR');
INSERT INTO Employees VALUES (101, 'Alice', 1), (102, 'Bob', 2);

-- Foreign key constraint prevents invalid references
-- INSERT INTO Employees VALUES (103, 'Charlie', 999); -- ERROR: dept_id 999 doesn't exist
```

**Key Takeaway:**
Primary keys ensure unique records; Foreign keys link tables and maintain referential integrity.

---

### Q6. What is Normalization? 🟢

**Definition:**
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves dividing large tables into smaller ones and defining relationships between them.

**Why it matters:**
Normalized databases avoid update anomalies, save storage space, and maintain data consistency.

**Goals of Normalization:**
1. Eliminate redundant data
2. Ensure data dependencies make sense
3. Reduce insert/update/delete anomalies

**Example - Before Normalization:**
```sql
-- Unnormalized table with redundancy
CREATE TABLE Orders_Bad (
    order_id INT,
    customer_name VARCHAR(50),
    customer_email VARCHAR(50),
    product_name VARCHAR(50),
    product_price DECIMAL(10,2)
);

-- Problem: Customer info repeated for every order
INSERT INTO Orders_Bad VALUES 
(1, 'Alice', 'alice@email.com', 'Laptop', 999.99),
(2, 'Alice', 'alice@email.com', 'Mouse', 25.99),  -- Redundant customer data
(3, 'Bob', 'bob@email.com', 'Keyboard', 75.00);
```

**After Normalization:**
```sql
-- Normalized design
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
```

**Key Takeaway:**
Normalization eliminates redundancy by splitting data into related tables, improving data integrity and efficiency.

---

### Q7. Normal Forms (1NF, 2NF, 3NF) 🟢

**Definition:**
Normal forms are progressive levels of database normalization, each building on the previous:

**1NF (First Normal Form):**
- Each column contains atomic (indivisible) values
- No repeating groups
- Each row is unique

**2NF (Second Normal Form):**
- Must be in 1NF
- No partial dependencies (all non-key attributes fully depend on primary key)

**3NF (Third Normal Form):**
- Must be in 2NF
- No transitive dependencies (non-key attributes don't depend on other non-key attributes)

**Why it matters:**
Each normal form removes specific types of anomalies and redundancy.

**Examples:**

**Violates 1NF (Non-atomic values):**
```sql
-- BAD: Phone column has multiple values
CREATE TABLE Students_Bad (
    id INT,
    name VARCHAR(50),
    phones VARCHAR(100)  -- "123-456, 789-012" - NOT ATOMIC
);
```

**1NF Corrected:**
```sql
CREATE TABLE Students (
    id INT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE StudentPhones (
    id INT,
    phone VARCHAR(15),
    PRIMARY KEY (id, phone),
    FOREIGN KEY (id) REFERENCES Students(id)
);
```

**Violates 2NF (Partial dependency):**
```sql
-- Composite key (student_id, course_id)
-- instructor_name depends only on course_id (partial dependency)
CREATE TABLE Enrollments_Bad (
    student_id INT,
    course_id INT,
    student_name VARCHAR(50),
    instructor_name VARCHAR(50),  -- Depends only on course_id
    PRIMARY KEY (student_id, course_id)
);
```

**2NF Corrected:**
```sql
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    instructor_name VARCHAR(50)
);

CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```

**Violates 3NF (Transitive dependency):**
```sql
-- department_location depends on department_id (transitive dependency)
CREATE TABLE Employees_Bad (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department_id INT,
    department_location VARCHAR(50)  -- Depends on department_id, not emp_id
);
```

**3NF Corrected:**
```sql
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    location VARCHAR(50)
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
```

**Key Takeaway:**
1NF = atomic values, 2NF = no partial dependencies, 3NF = no transitive dependencies.

---

### Q8. What are Constraints? 🟢

**Definition:**
Constraints are rules applied to database columns to enforce data integrity and validity. They ensure that data entered into the database meets specific criteria.

**Why it matters:**
Constraints prevent invalid data from entering the database, maintaining data quality and consistency.

**Types of Constraints:**

| Constraint | Purpose | Example |
|------------|---------|---------|
| **NOT NULL** | Column cannot have NULL values | `age INT NOT NULL` |
| **UNIQUE** | All values must be unique | `email VARCHAR(50) UNIQUE` |
| **PRIMARY KEY** | Unique identifier (NOT NULL + UNIQUE) | `id INT PRIMARY KEY` |
| **FOREIGN KEY** | Links to another table | `FOREIGN KEY (dept_id) REFERENCES Departments(id)` |
| **CHECK** | Values must satisfy a condition | `CHECK (age >= 18)` |
| **DEFAULT** | Default value if none provided | `status VARCHAR(20) DEFAULT 'active'` |

**Code Examples:**
```sql
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,                    -- PRIMARY KEY
    emp_name VARCHAR(50) NOT NULL,             -- NOT NULL
    email VARCHAR(100) UNIQUE,                 -- UNIQUE
    age INT CHECK (age >= 18 AND age <= 65),   -- CHECK
    department_id INT,
    salary DECIMAL(10,2) DEFAULT 30000.00,     -- DEFAULT
    status VARCHAR(20) DEFAULT 'active',
    FOREIGN KEY (department_id) REFERENCES Departments(dept_id)  -- FOREIGN KEY
);

-- Test constraints
INSERT INTO Employees (emp_id, emp_name, email, age) 
VALUES (1, 'Alice', 'alice@company.com', 25);  -- Success

-- INSERT INTO Employees (emp_id, emp_name, age) 
-- VALUES (2, NULL, 30);  -- ERROR: NOT NULL constraint

-- INSERT INTO Employees (emp_id, emp_name, email, age) 
-- VALUES (3, 'Bob', 'alice@company.com', 30);  -- ERROR: UNIQUE constraint

-- INSERT INTO Employees (emp_id, emp_name, email, age) 
-- VALUES (4, 'Charlie', 'charlie@company.com', 15);  -- ERROR: CHECK constraint
```

**Key Takeaway:**
Constraints enforce data integrity at the database level, preventing invalid data and maintaining consistency.

---

### Q9. ACID Properties 🟢

**Definition:**
ACID is a set of properties that guarantee reliable transaction processing in databases:

- **A**tomicity: All or nothing - transaction either completes fully or not at all
- **C**onsistency: Database moves from one valid state to another
- **I**solation: Concurrent transactions don't interfere with each other
- **D**urability: Once committed, data persists even after system failure

**Why it matters:**
ACID properties ensure data reliability, especially critical for financial transactions, e-commerce, and banking systems.

**Real-World Example:**
```sql
-- Bank transfer: Move $100 from Account A to Account B
BEGIN TRANSACTION;

-- Atomicity: Both operations must succeed, or both must fail
UPDATE Accounts SET balance = balance - 100 WHERE account_id = 'A';
UPDATE Accounts SET balance = balance + 100 WHERE account_id = 'B';

-- If any error occurs, ROLLBACK ensures atomicity
-- If both succeed, COMMIT ensures durability
COMMIT;
```

**Detailed Explanation:**

**1. Atomicity:**
```sql
BEGIN TRANSACTION;
UPDATE Inventory SET quantity = quantity - 1 WHERE product_id = 1;
INSERT INTO Orders (product_id, customer_id) VALUES (1, 100);
-- If INSERT fails, UPDATE is rolled back automatically
COMMIT;
```

**2. Consistency:**
```sql
-- Constraint ensures consistency
ALTER TABLE Accounts ADD CONSTRAINT check_balance CHECK (balance >= 0);
-- Any transaction that violates this is rejected
```

**3. Isolation:**
```sql
-- Transaction 1
BEGIN TRANSACTION;
SELECT balance FROM Accounts WHERE id = 1;  -- Reads $1000
-- ... some processing ...
UPDATE Accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Transaction 2 (concurrent)
-- Cannot see uncommitted changes from Transaction 1
BEGIN TRANSACTION;
SELECT balance FROM Accounts WHERE id = 1;  -- Still reads $1000 until T1 commits
COMMIT;
```

**4. Durability:**
```sql
COMMIT;  -- After this, data is permanently saved
-- Even if power fails immediately, changes persist
```

**Key Takeaway:**
ACID properties (Atomicity, Consistency, Isolation, Durability) ensure reliable and safe transaction processing in databases.

---

### Q10. What is a Transaction? 🟢

**Definition:**
A transaction is a logical unit of work that contains one or more SQL operations. It's an "all or nothing" proposition - either all operations succeed and the transaction is committed, or if any operation fails, the entire transaction is rolled back.

**Why it matters:**
Transactions ensure data integrity when multiple related operations must be performed together.

**Transaction Commands:**
- `BEGIN TRANSACTION` / `START TRANSACTION`: Start a transaction
- `COMMIT`: Permanently save all changes
- `ROLLBACK`: Undo all changes since transaction began
- `SAVEPOINT`: Create a point to rollback to

**Code Example:**
```sql
-- Example: Book flight tickets (must be atomic)
BEGIN TRANSACTION;

-- Step 1: Check seat availability
SELECT * FROM Flights WHERE flight_id = 101 AND available_seats > 0;

-- Step 2: Book seat
UPDATE Flights SET available_seats = available_seats - 1 WHERE flight_id = 101;

-- Step 3: Create booking record
INSERT INTO Bookings (customer_id, flight_id, seat_number) 
VALUES (500, 101, '12A');

-- Step 4: Process payment
INSERT INTO Payments (booking_id, amount, status) 
VALUES (LAST_INSERT_ID(), 250.00, 'paid');

-- If all succeed, commit
COMMIT;

-- If any fails, rollback
-- ROLLBACK;
```

**With Savepoints:**
```sql
BEGIN TRANSACTION;

UPDATE Accounts SET balance = balance - 100 WHERE id = 1;
SAVEPOINT after_debit;

UPDATE Accounts SET balance = balance + 100 WHERE id = 2;
-- If this fails, can rollback to savepoint
-- ROLLBACK TO after_debit;

COMMIT;
```

**Key Takeaway:**
Transactions group related operations into atomic units, ensuring data integrity through COMMIT/ROLLBACK mechanisms.

---

### Q11. SELECT, WHERE, ORDER BY 🟢

**Definition:**
- **SELECT**: Retrieves data from tables
- **WHERE**: Filters rows based on conditions
- **ORDER BY**: Sorts results in ascending or descending order

**Why it matters:**
These are the most fundamental SQL operations used in every query.

**Code Examples:**
```sql
-- Basic SELECT
SELECT * FROM Employees;
SELECT name, salary FROM Employees;

-- WHERE clause
SELECT * FROM Employees WHERE salary > 50000;
SELECT * FROM Employees WHERE department = 'IT' AND age > 25;

-- ORDER BY
SELECT * FROM Employees ORDER BY salary DESC;
SELECT * FROM Employees ORDER BY department ASC, salary DESC;

-- Combined
SELECT name, salary 
FROM Employees 
WHERE department = 'IT' 
ORDER BY salary DESC 
LIMIT 10;

-- WHERE with various operators
SELECT * FROM Products WHERE price BETWEEN 100 AND 500;
SELECT * FROM Customers WHERE name LIKE 'A%';
SELECT * FROM Orders WHERE customer_id IN (1, 2, 3);
SELECT * FROM Employees WHERE manager_id IS NULL;
```

**Key Takeaway:**
SELECT retrieves data, WHERE filters it, ORDER BY sorts it - the foundation of SQL queries.

---

### Q12. Aggregate Functions 🟢

**Definition:**
Aggregate functions perform calculations on multiple rows and return a single result.

**Common Functions:**
- **COUNT()**: Counts rows
- **SUM()**: Adds values
- **AVG()**: Calculates average
- **MIN()**: Finds minimum
- **MAX()**: Finds maximum

**Code Examples:**
```sql
-- COUNT
SELECT COUNT(*) as total_employees FROM Employees;
SELECT COUNT(DISTINCT department) as dept_count FROM Employees;

-- SUM
SELECT SUM(salary) as total_payroll FROM Employees;
SELECT SUM(quantity * price) as total_revenue FROM Orders;

-- AVG
SELECT AVG(salary) as avg_salary FROM Employees;
SELECT department, AVG(age) as avg_age FROM Employees GROUP BY department;

-- MIN and MAX
SELECT MIN(salary) as lowest, MAX(salary) as highest FROM Employees;

-- Multiple aggregates
SELECT 
    COUNT(*) as count,
    AVG(salary) as avg_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary
FROM Employees;
```

**Key Takeaway:**
Aggregate functions summarize data: COUNT for counting, SUM for totals, AVG for averages, MIN/MAX for extremes.

---

### Q13. GROUP BY vs HAVING 🟢

**Definition:**
- **GROUP BY**: Groups rows with same values into summary rows
- **HAVING**: Filters groups (used with GROUP BY, like WHERE for groups)

**Difference:**
- WHERE filters rows BEFORE grouping
- HAVING filters groups AFTER aggregation

**Code Examples:**
```sql
-- GROUP BY
SELECT department, COUNT(*) as emp_count
FROM Employees
GROUP BY department;

-- GROUP BY with multiple columns
SELECT department, job_title, AVG(salary) as avg_sal
FROM Employees
GROUP BY department, job_title;

-- WHERE vs HAVING
-- WHERE: Filter before grouping
SELECT department, AVG(salary) as avg_salary
FROM Employees
WHERE salary > 30000  -- Filter individual rows first
GROUP BY department;

-- HAVING: Filter after grouping
SELECT department, AVG(salary) as avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 50000;  -- Filter groups

-- Combined
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM Employees
WHERE hire_date > '2020-01-01'  -- Filter rows
GROUP BY department
HAVING COUNT(*) > 5  -- Filter groups
ORDER BY avg_salary DESC;
```

**Key Takeaway:**
GROUP BY creates groups; HAVING filters those groups. WHERE filters before grouping, HAVING filters after.

---

### Q14. What are Indexes? 🟢

**Definition:**
An index is a database structure that improves the speed of data retrieval operations. It's like a book's index - you can find information quickly without scanning every page.

**Why it matters:**
Indexes dramatically speed up SELECT queries but slow down INSERT/UPDATE/DELETE operations.

**Types of Indexes:**
1. **Primary Index**: Automatically created on primary key
2. **Unique Index**: Ensures column values are unique
3. **Composite Index**: Index on multiple columns
4. **Full-text Index**: For text searching

**Code Examples:**
```sql
-- Create index
CREATE INDEX idx_lastname ON Employees(last_name);

-- Composite index
CREATE INDEX idx_dept_salary ON Employees(department, salary);

-- Unique index
CREATE UNIQUE INDEX idx_email ON Employees(email);

-- View indexes
SHOW INDEX FROM Employees;

-- Drop index
DROP INDEX idx_lastname ON Employees;

-- Query without index (slow)
SELECT * FROM Employees WHERE last_name = 'Smith';  -- Full table scan

-- Query with index (fast)
-- Same query but uses idx_lastname for quick lookup
```

**When to Use Indexes:**
✅ Columns frequently used in WHERE clauses
✅ Columns used in JOIN conditions
✅ Columns used in ORDER BY
❌ Small tables (overhead not worth it)
❌ Columns frequently updated
❌ Columns with low cardinality (few unique values)

**Key Takeaway:**
Indexes speed up reads but slow down writes. Use them on frequently queried columns.

---

### Q15. DELETE vs TRUNCATE vs DROP 🟢

**Definition:**
Three commands to remove data/objects, each with different purposes and behaviors.

**Comparison:**

| Aspect | DELETE | TRUNCATE | DROP |
|--------|--------|----------|------|
| **Type** | DML | DDL | DDL |
| **Purpose** | Remove specific rows | Remove all rows | Remove entire table |
| **WHERE** | Can use WHERE | No WHERE clause | N/A |
| **Rollback** | Yes (with transaction) | No | No |
| **Speed** | Slower | Faster | Fastest |
| **Identity Reset** | No | Yes | N/A |
| **Triggers** | Fires DELETE triggers | Doesn't fire triggers | N/A |

**Code Examples:**
```sql
-- DELETE: Remove specific rows
DELETE FROM Employees WHERE department = 'IT';
DELETE FROM Employees WHERE salary < 30000;

-- DELETE all rows (can rollback)
BEGIN TRANSACTION;
DELETE FROM Employees;
ROLLBACK;  -- Data restored

-- TRUNCATE: Remove all rows (faster, cannot rollback)
TRUNCATE TABLE Employees;
-- Cannot use WHERE clause
-- Resets auto-increment counter

-- DROP: Remove entire table structure
DROP TABLE Employees;
-- Table no longer exists
-- Cannot rollback

-- Real example scenario
-- Remove old logs (DELETE with WHERE)
DELETE FROM Logs WHERE log_date < DATE_SUB(NOW(), INTERVAL 90 DAY);

-- Clear test data (TRUNCATE - fast)
TRUNCATE TABLE TestOrders;

-- Remove deprecated table (DROP)
DROP TABLE OldCustomers;
```

**Key Takeaway:**
DELETE removes specific rows (rollbackable), TRUNCATE clears all rows (fast), DROP removes entire table.

---

## INTERMEDIATE LEVEL QUESTIONS

### Q16. Types of Joins 🟡

**Definition:**
Joins combine rows from two or more tables based on related columns.

**Types:**
1. **INNER JOIN**: Returns matching rows from both tables
2. **LEFT JOIN**: All rows from left + matching from right
3. **RIGHT JOIN**: All rows from right + matching from left
4. **FULL OUTER JOIN**: All rows from both tables
5. **CROSS JOIN**: Cartesian product (all combinations)

**Code Examples:**
```sql
-- Sample tables
CREATE TABLE Employees (emp_id INT, name VARCHAR(50), dept_id INT);
CREATE TABLE Departments (dept_id INT, dept_name VARCHAR(50));

INSERT INTO Employees VALUES (1, 'Alice', 10), (2, 'Bob', 20), (3, 'Charlie', NULL);
INSERT INTO Departments VALUES (10, 'IT'), (20, 'HR'), (30, 'Finance');

-- INNER JOIN (only matching records)
SELECT e.name, d.dept_name
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;
-- Result: Alice-IT, Bob-HR (Charlie excluded, Finance excluded)

-- LEFT JOIN (all from left table)
SELECT e.name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id;
-- Result: Alice-IT, Bob-HR, Charlie-NULL

-- RIGHT JOIN (all from right table)
SELECT e.name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;
-- Result: Alice-IT, Bob-HR, NULL-Finance

-- FULL OUTER JOIN (all from both)
SELECT e.name, d.dept_name
FROM Employees e
FULL OUTER JOIN Departments d ON e.dept_id = d.dept_id;
-- Result: Alice-IT, Bob-HR, Charlie-NULL, NULL-Finance

-- CROSS JOIN (cartesian product)
SELECT e.name, d.dept_name
FROM Employees e
CROSS JOIN Departments d;
-- Result: 3 employees × 3 departments = 9 rows
```

**Key Takeaway:**
INNER JOIN: matching only. LEFT/RIGHT: all from one side. FULL OUTER: all from both. CROSS: all combinations.

---

### Q17. INNER vs OUTER JOIN 🟡

**Definition:**
- **INNER JOIN**: Returns only rows with matches in BOTH tables
- **OUTER JOIN**: Returns all rows from one or both tables, with NULLs for non-matches

**Code Examples:**
```sql
-- Setup
CREATE TABLE Orders (order_id INT, customer_id INT, amount DECIMAL(10,2));
CREATE TABLE Customers (customer_id INT, name VARCHAR(50));

INSERT INTO Orders VALUES (1, 101, 500), (2, 102, 300), (3, 999, 150);
INSERT INTO Customers VALUES (101, 'Alice'), (102, 'Bob'), (103, 'Charlie');

-- INNER JOIN: Only orders with valid customers
SELECT o.order_id, c.name, o.amount
FROM Orders o
INNER JOIN Customers c ON o.customer_id = c.customer_id;
-- Result: 2 rows (order_id 1, 2)
-- Order 3 excluded (no matching customer)
-- Charlie excluded (no orders)

-- LEFT OUTER JOIN: All orders, even without customer
SELECT o.order_id, c.name, o.amount
FROM Orders o
LEFT JOIN Customers c ON o.customer_id = c.customer_id;
-- Result: 3 rows
-- Order 3 shows: 3, NULL, 150

-- RIGHT OUTER JOIN: All customers, even without orders
SELECT o.order_id, c.name, o.amount
FROM Orders o
RIGHT JOIN Customers c ON o.customer_id = c.customer_id;
-- Result: 3 rows
-- Charlie shows: NULL, Charlie, NULL

-- Find customers with no orders (using LEFT JOIN)
SELECT c.name
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
-- Result: Charlie
```

**Key Takeaway:**
INNER JOIN requires matches in both tables. OUTER JOIN includes non-matching rows with NULLs.

---

### Q18. Self Join and Cross Join 🟡

**Definition:**
- **Self Join**: Join a table to itself to compare rows within the same table
- **Cross Join**: Cartesian product of two tables (every row with every row)

**Code Examples:**
```sql
-- SELF JOIN: Find employees and their managers
CREATE TABLE Employees (
    emp_id INT,
    name VARCHAR(50),
    manager_id INT
);

INSERT INTO Employees VALUES 
(1, 'Alice', NULL),  -- CEO
(2, 'Bob', 1),       -- Reports to Alice
(3, 'Charlie', 1),   -- Reports to Alice
(4, 'David', 2);     -- Reports to Bob

SELECT e.name as Employee, m.name as Manager
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;
-- Result:
-- Alice, NULL
-- Bob, Alice
-- Charlie, Alice
-- David, Bob

-- Find pairs of employees in same department
CREATE TABLE Staff (id INT, name VARCHAR(50), dept INT);
INSERT INTO Staff VALUES (1, 'A', 10), (2, 'B', 10), (3, 'C', 20);

SELECT e1.name, e2.name
FROM Staff e1
JOIN Staff e2 ON e1.dept = e2.dept AND e1.id < e2.id;
-- Result: A-B (same dept, avoid duplicates)

-- CROSS JOIN: All product-size combinations
CREATE TABLE Products (product VARCHAR(20));
CREATE TABLE Sizes (size VARCHAR(10));

INSERT INTO Products VALUES ('T-Shirt'), ('Jeans');
INSERT INTO Sizes VALUES ('S'), ('M'), ('L');

SELECT p.product, s.size
FROM Products p
CROSS JOIN Sizes s;
-- Result: 2 products × 3 sizes = 6 combinations
-- T-Shirt-S, T-Shirt-M, T-Shirt-L, Jeans-S, Jeans-M, Jeans-L
```

**Key Takeaway:**
Self Join compares rows within same table. Cross Join creates all possible combinations.

---

### Q19. Subqueries and Nested Queries 🟡

**Definition:**
A subquery is a query nested inside another query. Used to break complex queries into logical parts.

**Types:**
1. **Single-row subquery**: Returns one row
2. **Multi-row subquery**: Returns multiple rows
3. **Correlated subquery**: References outer query

**Code Examples:**
```sql
-- Single-row subquery
SELECT name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

-- Multi-row subquery with IN
SELECT name
FROM Employees
WHERE dept_id IN (SELECT dept_id FROM Departments WHERE location = 'NYC');

-- Subquery with EXISTS
SELECT name
FROM Customers c
WHERE EXISTS (
    SELECT 1 FROM Orders o WHERE o.customer_id = c.customer_id
);

-- Correlated subquery (references outer query)
SELECT e1.name, e1.salary
FROM Employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM Employees e2
    WHERE e2.dept_id = e1.dept_id
);

-- Subquery in FROM clause (derived table)
SELECT dept, avg_salary
FROM (
    SELECT dept_id as dept, AVG(salary) as avg_salary
    FROM Employees
    GROUP BY dept_id
) AS dept_avg
WHERE avg_salary > 50000;

-- Subquery in SELECT clause
SELECT 
    name,
    salary,
    (SELECT AVG(salary) FROM Employees) as company_avg
FROM Employees;
```

**Key Takeaway:**
Subqueries nest queries within queries. Use for filtering, comparisons, and breaking complex logic into parts.

---

### Q20. Views in SQL 🟡

**Definition:**
A view is a virtual table based on a SQL query. It doesn't store data but provides a saved query that can be treated like a table.

**Why it matters:**
Views simplify complex queries, enhance security by limiting data access, and provide data abstraction.

**Code Examples:**
```sql
-- Create a simple view
CREATE VIEW HighEarners AS
SELECT emp_id, name, salary, department
FROM Employees
WHERE salary > 80000;

-- Query the view like a table
SELECT * FROM HighEarners;
SELECT name FROM HighEarners WHERE department = 'IT';

-- Create view with JOIN
CREATE VIEW EmployeeDepartments AS
SELECT e.emp_id, e.name, d.dept_name, e.salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;

-- Create view with aggregation
CREATE VIEW DepartmentStats AS
SELECT 
    dept_id,
    COUNT(*) as employee_count,
    AVG(salary) as avg_salary,
    MAX(salary) as max_salary
FROM Employees
GROUP BY dept_id;

-- Update view (updatable views)
CREATE VIEW ITEmployees AS
SELECT emp_id, name, salary
FROM Employees
WHERE department = 'IT';

UPDATE ITEmployees SET salary = salary * 1.1 WHERE emp_id = 5;

-- Drop view
DROP VIEW HighEarners;

-- Replace view
CREATE OR REPLACE VIEW HighEarners AS
SELECT emp_id, name, salary
FROM Employees
WHERE salary > 100000;  -- Changed threshold
```

**Benefits:**
✅ Simplify complex queries
✅ Security (hide sensitive columns)
✅ Data abstraction
✅ Reusability

**Key Takeaway:**
Views are saved queries that act like virtual tables, simplifying access to complex data.

---

### Q21. Stored Procedures 🟡

**Definition:**
Stored procedures are precompiled SQL code saved in the database that can be executed repeatedly. They accept parameters and can contain complex business logic.

**Code Examples:**
```sql
-- Create stored procedure
DELIMITER //
CREATE PROCEDURE GetEmployeesByDept(IN dept_name VARCHAR(50))
BEGIN
    SELECT emp_id, name, salary
    FROM Employees e
    JOIN Departments d ON e.dept_id = d.dept_id
    WHERE d.dept_name = dept_name;
END //
DELIMITER ;

-- Execute procedure
CALL GetEmployeesByDept('IT');

-- Procedure with OUT parameter
DELIMITER //
CREATE PROCEDURE GetEmployeeCount(IN dept_id INT, OUT emp_count INT)
BEGIN
    SELECT COUNT(*) INTO emp_count
    FROM Employees
    WHERE department_id = dept_id;
END //
DELIMITER ;

-- Use OUT parameter
CALL GetEmployeeCount(10, @count);
SELECT @count;
```

**Key Takeaway:**
Stored procedures encapsulate business logic in the database, improving performance and reusability.

---

### Q22. Triggers 🟡

**Definition:**
Triggers are special stored procedures that automatically execute when specific events occur (INSERT, UPDATE, DELETE).

**Code Examples:**
```sql
-- Create trigger to log changes
CREATE TRIGGER salary_audit
AFTER UPDATE ON Employees
FOR EACH ROW
BEGIN
    IF NEW.salary != OLD.salary THEN
        INSERT INTO SalaryAudit (emp_id, old_salary, new_salary, change_date)
        VALUES (NEW.emp_id, OLD.salary, NEW.salary, NOW());
    END IF;
END;

-- Trigger to prevent deletion
CREATE TRIGGER prevent_admin_delete
BEFORE DELETE ON Employees
FOR EACH ROW
BEGIN
    IF OLD.role = 'Admin' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete Admin users';
    END IF;
END;
```

**Key Takeaway:**
Triggers automatically enforce business rules and maintain audit trails.

---

### Q23. Cursor in SQL 🟡

**Definition:**
Cursor allows row-by-row processing of query results. Used when you need to process each row individually.

**Code Example:**
```sql
DELIMITER //
CREATE PROCEDURE ProcessEmployees()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_name VARCHAR(50);
    DECLARE emp_salary DECIMAL(10,2);
    
    DECLARE emp_cursor CURSOR FOR 
        SELECT name, salary FROM Employees;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN emp_cursor;
    
    read_loop: LOOP
        FETCH emp_cursor INTO emp_name, emp_salary;
        IF done THEN
            LEAVE read_loop;
        END IF;
        -- Process each row
        IF emp_salary < 50000 THEN
            UPDATE Employees SET salary = salary * 1.1 WHERE name = emp_name;
        END IF;
    END LOOP;
    
    CLOSE emp_cursor;
END //
DELIMITER ;
```

**Key Takeaway:**
Cursors process result sets row-by-row but should be avoided when set-based operations can work.

---

### Q24. BCNF (Boyce-Codd Normal Form) 🟡

**Definition:**
BCNF is a stricter version of 3NF. A table is in BCNF if for every functional dependency X→Y, X must be a superkey.

**Code Example:**
```sql
-- Violates BCNF
CREATE TABLE Teaching (
    teacher VARCHAR(50),
    subject VARCHAR(50),
    student VARCHAR(50),
    PRIMARY KEY (teacher, subject, student)
);
-- teacher → subject (teacher determines subject, but teacher is not a superkey)

-- Convert to BCNF
CREATE TABLE TeacherSubjects (
    teacher VARCHAR(50),
    subject VARCHAR(50),
    PRIMARY KEY (teacher)
);

CREATE TABLE StudentEnrollments (
    student VARCHAR(50),
    teacher VARCHAR(50),
    PRIMARY KEY (student, teacher),
    FOREIGN KEY (teacher) REFERENCES TeacherSubjects(teacher)
);
```

**Key Takeaway:**
BCNF eliminates all anomalies by ensuring every determinant is a candidate key.

---

### Q25. Functional Dependency 🟡

**Definition:**
A functional dependency A→B means A uniquely determines B. Understanding FDs is crucial for normalization.

**Types:**
- **Trivial**: A→A (always true)
- **Non-trivial**: A→B where B is not subset of A
- **Partial**: Part of composite key determines non-key attribute
- **Transitive**: A→B and B→C, therefore A→C

**Key Takeaway:**
Functional dependencies define how attributes relate and guide normalization decisions.

---

### Q26. Entity-Relationship Model 🟡

**Definition:**
ER model is a conceptual data model using entities (objects), attributes (properties), and relationships (connections).

**Components:**
- **Entity**: Object (Employee, Department)
- **Attribute**: Property (name, salary)
- **Relationship**: Connection (works_in, manages)
- **Cardinality**: 1:1, 1:N, N:M

**Key Takeaway:**
ER diagrams visualize database structure before implementation.

---

### Q27. Cardinality in DBMS 🟡

**Definition:**
Cardinality defines the number of occurrences in a relationship.

**Types:**
- **One-to-One (1:1)**: One employee has one passport
- **One-to-Many (1:N)**: One department has many employees
- **Many-to-Many (M:N)**: Many students enroll in many courses

**Code Example:**
```sql
-- 1:1 relationship
CREATE TABLE Employees (emp_id INT PRIMARY KEY, name VARCHAR(50));
CREATE TABLE Passports (passport_id INT PRIMARY KEY, emp_id INT UNIQUE,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id));

-- 1:N relationship
CREATE TABLE Departments (dept_id INT PRIMARY KEY, name VARCHAR(50));
CREATE TABLE Employees (emp_id INT PRIMARY KEY, dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id));

-- M:N relationship (requires junction table)
CREATE TABLE Students (student_id INT PRIMARY KEY, name VARCHAR(50));
CREATE TABLE Courses (course_id INT PRIMARY KEY, title VARCHAR(50));
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```

**Key Takeaway:**
Cardinality determines table relationships and foreign key placement.

---

### Q28. Clustered vs Non-Clustered Index 🟡

**Definition:**
- **Clustered**: Physically sorts table data, one per table (usually primary key)
- **Non-Clustered**: Separate structure with pointers, multiple allowed

**Comparison:**

| Aspect | Clustered | Non-Clustered |
|--------|-----------|---------------|
| **Storage** | Sorts actual data | Separate index structure |
| **Count** | One per table | Multiple per table |
| **Speed** | Faster for range queries | Faster for lookups |
| **Memory** | Less (no duplicate data) | More (stores pointers) |

**Key Takeaway:**
Clustered index sorts data physically; non-clustered creates separate lookup structure.

---

### Q29. B-Tree and B+ Tree 🟡

**Definition:**
- **B-Tree**: Self-balancing tree for disk-based storage, used in databases
- **B+ Tree**: Variant where all data is in leaf nodes, better for range queries

**Characteristics:**
- **B-Tree**: Data in all nodes, direct access
- **B+ Tree**: Data only in leaves, linked list for range scans

**Key Takeaway:**
B+ Trees are preferred in databases for efficient range queries and sequential access.

---

### Q30. Locking Mechanisms 🟡

**Definition:**
Locks prevent concurrent transactions from interfering with each other.

**Types:**
- **Shared Lock (S)**: Multiple reads allowed
- **Exclusive Lock (X)**: No other access allowed
- **Update Lock (U)**: Prevents deadlock during updates

**Levels:**
- **Row-level**: Locks individual rows
- **Page-level**: Locks database pages
- **Table-level**: Locks entire table

**Key Takeaway:**
Locks ensure data consistency in concurrent environments but can impact performance.

---

### Q31. Deadlock 🟡

**Definition:**
Deadlock occurs when two or more transactions wait for each other to release locks, creating a cycle.

**Example:**
```sql
-- Transaction 1
BEGIN TRANSACTION;
UPDATE Accounts SET balance = balance - 100 WHERE id = 1;  -- Locks row 1
-- ... waiting for row 2 ...
UPDATE Accounts SET balance = balance + 100 WHERE id = 2;  -- Blocked by T2
COMMIT;

-- Transaction 2 (concurrent)
BEGIN TRANSACTION;
UPDATE Accounts SET balance = balance - 50 WHERE id = 2;   -- Locks row 2
-- ... waiting for row 1 ...
UPDATE Accounts SET balance = balance + 50 WHERE id = 1;   -- Blocked by T1
COMMIT;
-- DEADLOCK!
```

**Prevention:**
- Lock resources in same order
- Use timeout mechanisms
- Reduce transaction duration

**Key Takeaway:**
Deadlocks occur when transactions wait circularly; prevent by ordering resource access.

---

### Q32. UNION vs UNION ALL 🟡

**Definition:**
Both combine results from multiple SELECT queries.
- **UNION**: Removes duplicates
- **UNION ALL**: Keeps all rows (faster)

**Code Examples:**
```sql
-- UNION (removes duplicates)
SELECT name FROM Employees WHERE dept = 'IT'
UNION
SELECT name FROM Employees WHERE dept = 'HR';

-- UNION ALL (keeps duplicates, faster)
SELECT name FROM Employees WHERE dept = 'IT'
UNION ALL
SELECT name FROM Employees WHERE dept = 'HR';

-- Columns must match
SELECT emp_id, name FROM Employees
UNION
SELECT customer_id, name FROM Customers;
```

**Key Takeaway:**
Use UNION ALL when duplicates are acceptable for better performance.

---

### Q33. Window Functions 🟡

**Definition:**
Window functions perform calculations across rows related to current row without grouping.

**Common Functions:**
- ROW_NUMBER(), RANK(), DENSE_RANK()
- SUM(), AVG(), COUNT() with OVER()
- LEAD(), LAG()

**Code Examples:**
```sql
-- ROW_NUMBER: Unique sequential number
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM Employees;

-- RANK: Rank with gaps for ties
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank
FROM Employees;

-- Partition by department
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM Employees;

-- Running total
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) as running_total
FROM Sales;

-- LAG and LEAD
SELECT name, salary,
       LAG(salary) OVER (ORDER BY hire_date) as prev_salary,
       LEAD(salary) OVER (ORDER BY hire_date) as next_salary
FROM Employees;
```

**Key Takeaway:**
Window functions enable complex analytics without grouping, preserving individual rows.

---

### Q34. CTE (Common Table Expression) 🟡

**Definition:**
CTE is a temporary named result set that exists within a single query. Makes complex queries readable.

**Code Examples:**
```sql
-- Basic CTE
WITH HighEarners AS (
    SELECT * FROM Employees WHERE salary > 80000
)
SELECT name, salary FROM HighEarners WHERE department = 'IT';

-- Multiple CTEs
WITH
DeptAvg AS (
    SELECT dept_id, AVG(salary) as avg_salary FROM Employees GROUP BY dept_id
),
HighPerformers AS (
    SELECT emp_id, name, dept_id, salary FROM Employees WHERE rating > 4
)
SELECT h.name, h.salary, d.avg_salary
FROM HighPerformers h
JOIN DeptAvg d ON h.dept_id = d.dept_id;

-- Recursive CTE (organizational hierarchy)
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT emp_id, name, manager_id, 1 as level
    FROM Employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.emp_id, e.name, e.manager_id, eh.level + 1
    FROM Employees e
    JOIN EmployeeHierarchy eh ON e.manager_id = eh.emp_id
)
SELECT * FROM EmployeeHierarchy ORDER BY level;
```

**Key Takeaway:**
CTEs improve query readability and enable recursive queries for hierarchical data.

---

### Q35. Data Warehousing Basics 🟡

**Definition:**
Data warehouse is a centralized repository for integrated data from multiple sources, optimized for analysis.

**Characteristics:**
- **Subject-oriented**: Organized by business area
- **Integrated**: Consistent data from various sources
- **Time-variant**: Historical data
- **Non-volatile**: Read-only, not updated

**Components:**
- **ETL**: Extract, Transform, Load
- **OLAP**: Online Analytical Processing
- **Data Marts**: Subset for specific departments

**Key Takeaway:**
Data warehouses store historical data for business intelligence and analytics, separate from operational databases.

---

## ADVANCED LEVEL QUESTIONS

### Q36. Query Optimization Techniques 🔴

**Techniques:**
1. **Use indexes** on frequently queried columns
2. **Avoid SELECT \***, specify needed columns
3. **Use EXPLAIN** to analyze query plans
4. **Optimize JOINs** (proper join order)
5. **Avoid subqueries** when JOINs work
6. **Use LIMIT** for large result sets
7. **Partition large tables**
8. **Update statistics** regularly

**Code Examples:**
```sql
-- Bad
SELECT * FROM Orders WHERE YEAR(order_date) = 2023;

-- Good
SELECT order_id, customer_id, amount 
FROM Orders 
WHERE order_date >= '2023-01-01' AND order_date < '2024-01-01';

-- Use EXPLAIN
EXPLAIN SELECT * FROM Employees WHERE department = 'IT';
```

**Key Takeaway:**
Optimize queries through proper indexing, avoiding full scans, and analyzing execution plans.

---

### Q37. CAP Theorem 🔴

**Definition:**
CAP Theorem states distributed systems can guarantee only 2 of 3:
- **Consistency**: All nodes see same data
- **Availability**: System always responds
- **Partition Tolerance**: Works despite network failures

**Examples:**
- **CA**: Traditional RDBMS (not partition-tolerant)
- **CP**: MongoDB, HBase (consistent, partition-tolerant)
- **AP**: Cassandra, DynamoDB (available, partition-tolerant)

**Key Takeaway:**
In distributed systems, choose 2 of CAP based on business needs.

---

### Q38. NoSQL vs SQL 🔴

**Comparison:**

| Aspect | SQL | NoSQL |
|--------|-----|-------|
| **Schema** | Fixed schema | Flexible schema |
| **Scaling** | Vertical (up) | Horizontal (out) |
| **ACID** | Full support | Eventual consistency |
| **Use Case** | Structured data, complex queries | Unstructured data, high volume |
| **Examples** | MySQL, PostgreSQL | MongoDB, Cassandra |

**Key Takeaway:**
SQL for structured data with ACID, NoSQL for scalability and flexible schema.

---

### Q39. Sharding and Partitioning 🔴

**Definition:**
- **Partitioning**: Split table into smaller pieces on same server
- **Sharding**: Distribute data across multiple servers

**Types:**
- **Horizontal**: Split rows
- **Vertical**: Split columns
- **Range**: By value ranges
- **Hash**: By hash function

**Code Example:**
```sql
-- Range partitioning
CREATE TABLE Orders (
    order_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024)
);
```

**Key Takeaway:**
Partitioning improves query performance; sharding enables horizontal scaling.

---

### Q40. Replication 🔴

**Definition:**
Replication copies data to multiple database servers for availability and load distribution.

**Types:**
- **Master-Slave**: One writes, multiple read
- **Master-Master**: Multiple writers
- **Synchronous**: Immediate consistency
- **Asynchronous**: Eventual consistency

**Key Takeaway:**
Replication improves availability and read performance through data redundancy.

---

### Q41-Q50. Advanced Topics Summary 🔴

**Q41. Two-Phase Commit**: Distributed transaction protocol ensuring atomicity across systems.

**Q42. Serializability**: Transactions execute as if serial, ensuring consistency.

**Q43. Phantom Read, Dirty Read**: Concurrency issues - dirty read sees uncommitted data, phantom read sees new rows.

**Q44. Isolation Levels**: Read Uncommitted, Read Committed, Repeatable Read, Serializable.

**Q45. Database Design Best Practices**: Normalize appropriately, use constraints, plan for scalability.

**Q46. OLTP vs OLAP**: OLTP for transactions (INSERT/UPDATE), OLAP for analytics (complex queries).

**Q47. Star Schema vs Snowflake**: Star has denormalized dimension tables, snowflake normalizes them.

**Q48. Horizontal vs Vertical Scaling**: Horizontal adds servers, vertical adds power to existing server.

**Q49. MVCC**: Multi-Version Concurrency Control allows multiple versions for concurrent access.

**Q50. Backup and Recovery**: Full, incremental, differential backups; point-in-time recovery.

---

## 📊 Key Comparison Tables

### SQL Commands Comparison

| Command | Category | Purpose | Rollback? | Example |
|---------|----------|---------|-----------|---------|
| **CREATE** | DDL | Create objects | No | `CREATE TABLE users` |
| **INSERT** | DML | Add data | Yes | `INSERT INTO users VALUES (1, 'Alice')` |
| **SELECT** | DQL | Query data | N/A | `SELECT * FROM users` |
| **GRANT** | DCL | Give permissions | No | `GRANT SELECT ON users TO john` |
| **COMMIT** | TCL | Save changes | N/A | `COMMIT;` |

### Normalization Forms Quick Reference

| Normal Form | Key Rule | Eliminates |
|-------------|----------|------------|
| **1NF** | Atomic values, no repeating groups | Repeating groups |
| **2NF** | 1NF + No partial dependencies | Partial dependencies |
| **3NF** | 2NF + No transitive dependencies | Transitive dependencies |
| **BCNF** | 3NF + Every determinant is a candidate key | Remaining anomalies |

### Keys Comparison

| Key Type | Unique? | NULL? | Count per Table | Purpose |
|----------|---------|-------|-----------------|---------|
| **Primary Key** | Yes | No | 1 | Unique identifier |
| **Foreign Key** | No | Yes | Multiple | Referential integrity |
| **Unique Key** | Yes | Yes (one NULL) | Multiple | Unique values |
| **Composite Key** | Yes | No | Multiple | Multi-column primary key |

---

## 🎯 Top 10 Most Asked Questions

1. **🟢 ACID Properties** - Foundation of database reliability
2. **🟢 Normalization (1NF, 2NF, 3NF)** - Most common design question
3. **🟡 Joins (INNER, LEFT, RIGHT, FULL)** - Query fundamentals
4. **🟢 Primary Key vs Foreign Key** - Relationship basics
5. **🟡 Indexes and their types** - Performance optimization
6. **🟡 Transactions and Isolation Levels** - Concurrency control
7. **🟢 DELETE vs TRUNCATE vs DROP** - Data removal operations
8. **🟡 Stored Procedures vs Triggers** - Database programming
9. **🔴 Query Optimization** - Performance tuning
10. **🟡 NoSQL vs SQL** - Modern database trends

---

## 📝 SQL Syntax Cheat Sheet

### Basic Queries
```sql
-- SELECT with conditions
SELECT column1, column2 FROM table WHERE condition ORDER BY column1 DESC;

-- JOIN
SELECT t1.col, t2.col FROM table1 t1 
JOIN table2 t2 ON t1.id = t2.foreign_id;

-- GROUP BY with HAVING
SELECT department, COUNT(*) as count FROM employees 
GROUP BY department HAVING count > 5;

-- Subquery
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

### Advanced Operations
```sql
-- Window Functions
SELECT name, salary, 
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM employees;

-- CTE (Common Table Expression)
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 100000
)
SELECT * FROM high_earners WHERE department = 'IT';

-- CASE Statement
SELECT name, 
       CASE 
           WHEN salary < 50000 THEN 'Low'
           WHEN salary < 100000 THEN 'Medium'
           ELSE 'High'
       END as salary_grade
FROM employees;
```

---

## 💡 Interview Tips

### Study Strategy
1. **Week 1**: Basic SQL (Q1-Q15) + Practice queries
2. **Week 2**: Joins, Subqueries, Normalization (Q16-Q25)
3. **Week 3**: Indexes, Transactions, Advanced topics (Q26-Q40)
4. **Week 4**: Optimization, NoSQL, System design (Q41-Q50)

### Common Mistakes to Avoid
❌ Not understanding the difference between WHERE and HAVING
❌ Forgetting to use FOREIGN KEY constraints
❌ Using SELECT * in production code
❌ Not considering NULL values in comparisons
❌ Ignoring query performance and indexing

### Interview Success Tips
✅ Always explain your thought process
✅ Draw ER diagrams when discussing design
✅ Mention trade-offs (normalization vs performance)
✅ Give real-world examples
✅ Know SQL syntax differences between MySQL, PostgreSQL, SQL Server

---

[⬆️ Back to Table of Contents](#-table-of-contents)

**Good luck with your DBMS interviews! 🚀**
