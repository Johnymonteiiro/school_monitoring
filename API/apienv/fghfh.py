import psycopg2

# Connect to the School database
conn = psycopg2.connect(
    dbname="school",
    user="postgres",
    password="your_password",
    host="localhost"
)