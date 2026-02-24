import sqlite3

#Each item will have the following attributes:
    #name, description, quantity, category, date last updated, and location


def createDatabase():   # This function creates the database with its table
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Inventory(
            ItemID INT PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Description VARCHAR(30),
            Category VARCHAR(30),
            Quantity INT,
            Location Varchar(30),
            LastUpdated DATE
            ) """
        
        
        cursor.execute(create_table_query)


        

def addItem():
    pass

def removeItem():
    pass

def updateItem():
    pass



cursor.execute("INSERT INTO Student (StudentId, Name, Major) VALUES (1, 'Alice', 'CS')")
