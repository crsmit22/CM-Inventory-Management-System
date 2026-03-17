from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)#Application Setup

#Create database on startup
database.createDatabase()

# Page Routes
@app.route("/")#Home page rout
def home():
    return render_template("index.html")

@app.route("/inventory")#Inventory page route
def inventory():
    return render_template("inventory.html")

@app.route("/contact")#Contact page route
def contact():
    return render_template("contact.html")

#API Routes
@app.route("/api/items", methods=["GET"])#Get all inventory items
def api_get_items():
    rows = database.getAllItems()
    items = []

    for r in rows:
        items.append({
            "ItemID": r["ItemID"],
            "Name": r["Name"],
            "Description": r["Description"],
            "Category": r["Category"],
            "Quantity": r["Quantity"],
            "Location": r["Location"],
            "LastUpdated": r["LastUpdated"],
        })

    return jsonify(items)


@app.route("/api/search", methods=["GET"])#Search inventory items
def api_search():
    q = request.args.get("q", "").strip()

    if not q:
        rows = database.getAllItems()
    else:
        rows = database.search(q)

    items = []
    for r in rows:
        items.append({
            "ItemID": r["ItemID"],
            "Name": r["Name"],
            "Description": r["Description"],
            "Category": r["Category"],
            "Quantity": r["Quantity"],
            "Location": r["Location"],
            "LastUpdated": r["LastUpdated"],
        })

    return jsonify(items)


@app.route("/api/items", methods=["POST"])#Add a new inventory item
def api_add_item():
    data = request.get_json(force=True)

    n = data.get("Name", "")
    d = data.get("Description", "")
    c = data.get("Category", "")
    q = data.get("Quantity", 0)
    l = data.get("Location", "")

    database.addItem(n, d, c, q, l)
    return jsonify({"ok": True})


@app.route("/api/items/<int:item_id>", methods=["PUT"])# Delete an inventory item
def api_update_item(item_id):
    data = request.get_json(force=True)

    n = data.get("Name", "")
    d = data.get("Description", "")
    c = data.get("Category", "")
    q = data.get("Quantity", 0)
    l = data.get("Location", "")

    database.updateItem(item_id, n, d, c, q, l)
    return jsonify({"ok": True})


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def api_delete_item(item_id):
    database.removeItem(item_id)
    return jsonify({"ok": True})

#Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)