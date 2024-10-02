import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'juanalvarez04',
    
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dbcrud") 

print("All done")