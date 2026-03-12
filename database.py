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
