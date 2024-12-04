# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print('All done')
