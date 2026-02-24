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

