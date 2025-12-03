import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

# Part 2 – Basic Queries

expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""


avg_hire_age = """
SELECT AVG((julianday(HireDate) - julianday(BirthDate)) / 365.25)
FROM Employee;
"""


# Part 3 – JOIN Queries

ten_most_expensive = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier ON Supplier.Id = Product.SupplierId
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""


largest_category = """
SELECT Category.CategoryName, COUNT(Product.Id) AS product_count
FROM Category
JOIN Product ON Product.CategoryId = Category.Id
GROUP BY Category.Id
ORDER BY product_count DESC
LIMIT 1;
"""


if __name__ == "__main__":
    print("Testing queries...")

    print("\nTop 10 expensive items:")
    print(curs.execute(expensive_items).fetchall())

    print("\nAverage hire age:")
    print(curs.execute(avg_hire_age).fetchall())

    print("\nTop 10 expensive items with suppliers:")
    print(curs.execute(ten_most_expensive).fetchall())

    print("\nLargest category:")
    print(curs.execute(largest_category).fetchall())

conn.close()
