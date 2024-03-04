import mysql.connector

# Establish the connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="ApocalypseBot"
)

# Create a cursor to execute queries
cursor = db.cursor()
