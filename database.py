import sqlite3

#Each item will have the following attributes:
    #name, description, quantity, category, date last updated, and location


def createDatabase():
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()

        

def addItem():
    pass

def removeItem():
    pass

def updateItem():
    pass

create_table_query="""
CREATE TABLE IF NOT EXISTS Student(
  StudentId INT,
  Name VARCHAR(50),
  Major VARCHAR(30),
  CONSTRAINT Student_PK PRIMARY KEY(StudentId)
)"""
cursor.execute(create_table_query)

cursor.execute("INSERT INTO Student (StudentId, Name, Major) VALUES (1, 'Alice', 'CS')")
