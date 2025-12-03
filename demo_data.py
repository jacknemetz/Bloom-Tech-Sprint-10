import sqlite3

# 1. Connect to the database
conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()

# 2. Create the 'demo' table
create_table_query = '''
CREATE TABLE IF NOT EXISTS demo (
    s TEXT,
    x INTEGER,
    y INTEGER
);
'''
cursor.execute(create_table_query)

# 3. Define the data to be inserted
data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7),
    ('p', 5, 6),
    ('z', 6, 9),
    ('l', 5, 4),
    ('q', 8, 7)
]

# 4. Insert data into the table
insert_query = 'INSERT INTO demo (s, x, y) VALUES (?, ?, ?);'
cursor.executemany(insert_query, data)

# 5. Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'demo_data.sqlite3' created, table 'demo' created, and data inserted successfully.")

# Reconnect to the database for querying
conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()

# 1. Total number of rows
row_count_query = 'SELECT COUNT(*) FROM demo;'
cursor.execute(row_count_query)
row_count = cursor.fetchall()
print(f"Total number of rows: {row_count}")

# 2. Number of rows where both x and y are at least 5
xy_at_leas_5_query = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;'
cursor.execute(xy_at_leas_5_query)
xy_at_leas_5 = cursor.fetchall()
print(f"Number of rows where x and y are at least 5: {xy_at_leas_5}")

# 3. Number of unique y values
unique_y_query = 'SELECT COUNT(DISTINCT y) FROM demo;'
cursor.execute(unique_y_query)
unique_y = cursor.fetchall()
print(f"Number of unique y values: {unique_y}")

# Close the connection
conn.close()
