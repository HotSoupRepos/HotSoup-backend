import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="postgres",
    user="admin",
    password="postgres",
    host="0.0.0.0"
)

# Open cursor to perform database operation
cur = conn.cursor()

#insert data
#cur.execute("INSERT INTO localsoupkitchens(name,age) VALUES ('Claudia',11)")

# Query the database 
cur.execute("SELECT * FROM localsoupkitchens")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close communications with database
cur.close()
conn.close()