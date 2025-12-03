import sqlite3

# Connect to the Northwind database
conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()

# SQL query to retrieve the ten most expensive items
expensive_items = '''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''

# SQL query to calculate the average age of employees at hiring
avg_hire_age = '''
SELECT AVG((julianday(HireDate) - julianday(BirthDate)) / 365.25)
FROM Employee;
'''

# Print the queries to verify (optional, will be removed for final execution of queries)
print("Defined expensive_items query:", expensive_items)
print("Defined avg_hire_age query:", avg_hire_age)

# Close the connection for now. It will be reopened for actual query execution later.
conn.close()

# Reconnect to the database for defining new queries
conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()

# SQL query to retrieve ProductName, UnitPrice, and CompanyName for the ten most expensive items
ten_most_expensive = '''
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
'''

# SQL query to identify the category with the largest number of unique products
largest_category = '''
SELECT Category.CategoryName, COUNT(Product.Id) AS product_count
FROM Category
JOIN Product ON Product.CategoryId = Category.Id
GROUP BY Category.Id
ORDER BY product_count DESC
LIMIT 1;
'''

# Print the new queries to verify
print("Defined ten_most_expensive query:", ten_most_expensive)
print("Defined largest_category query:", largest_category)

# Close the connection
conn.close()
