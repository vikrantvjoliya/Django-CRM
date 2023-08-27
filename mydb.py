import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Vikrant$123'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE VK")

print("ALL Done")