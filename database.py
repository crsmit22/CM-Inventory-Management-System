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

def addItem(n, d, c, q, l): # Function adds an element to the database
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        addQuery = """
                INSERT INTO Inventory (Name, Description, Category, Quantity, Location, LastUpdated) VALUES 
                   (?, ?, ?, ?, ?, ?)
                """
        cursor.execute(addQuery, (n, d, c, q, l, date.today()))
    #return print(f"Successfully added {n}")

def removeItem(itemID): # Function takes item ID. Deletes item by ID.

    searchQuerey = """
        DELETE FROM Inventory WHERE ItemID = ?
"""
    
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()

        cursor.execute(searchQuerey, (itemID))

def updateItem(itemID, n, d, c, q, l): # Function takes an item ID and updates said item
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        updateQuery = """
            UPDATE Inventory
            SET
                name = ?,
                description = ?,
                category = ?,
                quantity = ?,
                location = ?,
                LastUpdated = ?
            WHERE ItemId = ?;
        """

        cursor.execute(updateQuery, (n, d, c, q, l, date.today(), itemID))
    


# """INSERT INTO Inventory (Name, Description, Category, Quantity, Location, LastUpdated) VALUES 
#  ('Luna', 'Glass container to hold the Eucharist in a Monstrance', 'Sacred Vessels', 1, 'Tabernacle', 2026-02-22),
#  ('Cruet', 'holds the water and the wine for Mass', 'Glassware', 2, 'Minifridge', 2026-01-20),
#  ('Main Candle Extinguisher', 'extinguishes candles', null, 1, 'Sacristy Closet Door', 2026-01-20),
#  ('Small hosts tub', 'unconsecrated hosts used for Mass, 1 3/8in', 'Supplies', 5, 'Hosts Cabinet', 2025-02-20),
#  ('Purificator', 'used to clean sacred vessels', 'Linens', 15, 'Liturgy Linens', 2020-11-30),
#  ('Lavabo Towel', 'used for Fr. to dry his wet hands before consecration', 'Linens', 2, 'Liturgy Linens', 2022-05-13);"""