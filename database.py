import sqlite3

#Each item will have the following attributes:
    #name, description, quantity, category, date last updated, and location


def createDatabase():   # This function creates the database with its table
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Inventory(
            ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Description VARCHAR(30),
            Category VARCHAR(30),
            Quantity INT,
            Location Varchar(30),
            LastUpdated DATE
            ) """
        
        
        cursor.execute(create_table_query)


def search(searchWord): # Search function takes one search string and looks for match in Name, Category, or Location
                        # Returns a list of Tuples that contain all the data for each row of matches

    searchQuerey = """
        SELECT * FROM Inventory WHERE
        Name = ? OR Category = ? OR Location = ?"""
    
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()

        cursor.execute(searchQuerey, (searchWord, searchWord, searchWord))

        rows = cursor.fetchall()

    return rows


def addItem():
    pass

def removeItem():
    pass

def updateItem():
    pass



cursor.execute("INSERT INTO Student (StudentId, Name, Major) VALUES (1, 'Alice', 'CS')")
