import sqlite3

#Each item will have the following attributes:
    #name, description, quantity, category, date last updated, and location


def createDatabase():   # This function creates the database with its table
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()

        
        
        cursor.execute(create_table_query)


        

def addItem():
    pass

def removeItem():
    pass

def updateItem():
    pass



cursor.execute("INSERT INTO Student (StudentId, Name, Major) VALUES (1, 'Alice', 'CS')")
