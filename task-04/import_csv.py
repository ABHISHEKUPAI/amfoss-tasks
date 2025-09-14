# import_csv.py
import mysql.connector
import csv

# --- Database connection ---
conn = mysql.connector.connect(
    host="localhost",
    user="abhishek",       # change if needed
    password="krishna123", # change if needed
    database="cinescope_db"
)
cursor = conn.cursor()

# --- Create table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    genre VARCHAR(255),
    rating FLOAT,
    director VARCHAR(255),
    star1 VARCHAR(255),
    star2 VARCHAR(255),
    star3 VARCHAR(255)
)
""")

# --- Import CSV ---
with open("movies.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")  # change to "\t" if TSV
    next(reader)  # skip header row
    for row in reader:
        title, year, genre, rating, director, star1, star2, star3 = row
        year = int(year) if year else None
        rating = float(rating) if rating else None
        cursor.execute("""
            INSERT INTO movies (title, year, genre, rating, director, star1, star2, star3)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (title, year, genre, rating, director, star1, star2, star3))

# --- Save & close ---
conn.commit()
cursor.close()
conn.close()

print("Movies imported successfully!")
