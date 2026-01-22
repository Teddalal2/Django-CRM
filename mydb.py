# Install Mysql on your computer before running this code
# https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root  ", passwd="Nafi17830!")

# prepare a cursor object
cursorObject = dataBase.cursor()
# Create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
