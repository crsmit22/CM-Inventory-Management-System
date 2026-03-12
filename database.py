import sqlite3
from datetime import date

def createDatabase():
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS Inventory(
            ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Description VARCHAR(200),
            Category VARCHAR(30),
            Quantity INTEGER,
            Location VARCHAR(30),
            LastUpdated DATE
        )
        """

        cursor.execute(create_table_query)


def getAllItems():
    with sqlite3.connect("inventoryDB.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Inventory ORDER BY Name ASC")
        rows = cursor.fetchall()

    return rows


def search(searchWord):
    searchWord = f"%{searchWord}%"

    searchQuery = """
        SELECT * FROM Inventory
        WHERE Name LIKE ? OR Category LIKE ? OR Location LIKE ?
        ORDER BY Name ASC
    """

    with sqlite3.connect("inventoryDB.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(searchQuery, (searchWord, searchWord, searchWord))
        rows = cursor.fetchall()

    return rows


def addItem(n, d, c, q, l):
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        addQuery = """
            INSERT INTO Inventory
            (Name, Description, Category, Quantity, Location, LastUpdated)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(addQuery, (n, d, c, q, l, date.today()))


def removeItem(itemID):
    deleteQuery = "DELETE FROM Inventory WHERE ItemID = ?"

    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        cursor.execute(deleteQuery, (itemID,))


def updateItem(itemID, n, d, c, q, l):
    with sqlite3.connect("inventoryDB.db") as conn:
        cursor = conn.cursor()
        updateQuery = """
            UPDATE Inventory
            SET
                Name = ?,
                Description = ?,
                Category = ?,
                Quantity = ?,
                Location = ?,
                LastUpdated = ?
            WHERE ItemID = ?;
        """

        cursor.execute(updateQuery, (n, d, c, q, l, date.today(), itemID))

# instertString = """INSERT INTO Inventory (Name, Description, Category, Quantity, Location, LastUpdated) VALUES 
# ('Luna', 'Glass container to hold the Eucharist in a Monstrance', 'Sacred Vessels', 1, 'Tabernacle', 2026-02-22), 
# ('Cruet', 'holds the water and the wine for Mass', 'Glassware', 2, 'Minifridge', 2026-01-20), 
# ('Main Candle Extinguisher', 'extinguishes candles', null, 1, 'Sacristy Closet Door', 2026-01-20),
# ('Small hosts tub', 'unconsecrated hosts used for Mass, 1 3/8in', 'Supplies', 5, 'Hosts Cabinet', 2025-02-20),
# ('Purificator', 'used to clean sacred vessels', 'Linens', 15, 'Liturgy Linens', 2020-11-30), # ('Lavabo Towel', 'used for Fr. to dry his wet hands before consecration', 'Linens', 2, 'Liturgy Linens', 2022-05-13);""" 
# with sqlite3.connect("inventoryDB.db") as conn: # cursor = conn.cursor() # cursor.execute(instertString)
# print(search("candle")) 
# print(search("purificator")) 
# print(search("Candle"))