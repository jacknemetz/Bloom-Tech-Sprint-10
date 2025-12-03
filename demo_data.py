import sqlite3

# Connect to DB (creates file if missing)
conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()

# Drop table if re-running
curs.execute("DROP TABLE IF EXISTS demo;")

# Create table
curs.execute("""
CREATE TABLE demo (
    s TEXT,
    x INT,
    y INT
);
""")

# Insert data
rows = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

curs.executemany("INSERT INTO demo (s, x, y) VALUES (?, ?, ?);", rows)
conn.commit()

# Queries for CodeGrade variables
row_count = curs.execute("SELECT COUNT(*) FROM demo;").fetchall()

xy_at_least_5 = curs.execute("""
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5;
""").fetchall()

unique_y = curs.execute("""
SELECT COUNT(DISTINCT y)
FROM demo;
""").fetchall()

if __name__ == "__main__":
    print("row_count =", row_count)
    print("xy_at_least_5 =", xy_at_least_5)
    print("unique_y =", unique_y)

conn.close()
