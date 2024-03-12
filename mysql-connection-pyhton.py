# importing required libraries
# install pip3 install mysql-connector-python
import mysql.connector

dataBase = mysql.connector.connect(host="127.0.0.1", user="root", password="beehyv@123", database="oman")

print(dataBase)
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE Newtable (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""

# table created
cursorObject.execute(studentRecord)

sql = "INSERT INTO Newtable (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = [("Nikhil", "CSE", "98", "A", "18"),
       ("Nisha", "CSE", "99", "A", "18"),
       ("Rohan", "MAE", "43", "B", "20"),
       ("Amit", "ECE", "24", "A", "21"),
       ("Anil", "MAE", "45", "B", "20"),
       ("Megha", "ECE", "55", "A", "22"),
       ("Sita", "CSE", "95", "A", "19")]
cursorObject.executemany(sql, val)
dataBase.commit()

query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

query = "DELETE FROM STUDENT WHERE NAME = 'Ram'"
cursorObject.execute(query)
dataBase.commit()

query = "SELECT * FROM Newtable ORDER BY NAME DESC"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
       print(x)

query = "SELECT * FROM STUDENT LIMIT 2 OFFSET 1"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
       print(x)
# Disconnecting from the server
dataBase.close()
