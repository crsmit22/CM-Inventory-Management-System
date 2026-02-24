import sqlite3
from datetime import date

#Each item will have the following attributes:
    #name, description, quantity, category, date last updated, and location


def createDatabase():   # This function creates the database with its table
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Inventory(
            ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Description VARCHAR(200),
            Category VARCHAR(30),
            Quantity INTEGER,
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

def addItem(n, d, c, q, l):
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO Inventory (Name, Description, Category, Quantity, Location, LastUpdated) VALUES 
                   (n, d, c, q, l, date.today())"""
    )
    #return print(f"Successfully added {n}")

def removeItem(itemID): # Function takes item ID. Deletes item by ID.

    searchQuerey = """
        DELETE FROM Inventory WHERE ItemID = ?
"""
    
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()

        cursor.execute(searchQuerey, (itemID))

def updateItem():
    pass

