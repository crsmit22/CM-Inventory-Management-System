from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)

database.createDatabase()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/api/items", methods=["GET"])
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


@app.route("/api/search", methods=["GET"])
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


@app.route("/api/items", methods=["POST"])
def api_add_item():
    data = request.get_json(force=True)

    n = data.get("Name", "")
    d = data.get("Description", "")
    c = data.get("Category", "")
    q = data.get("Quantity", 0)
    l = data.get("Location", "")

    database.addItem(n, d, c, q, l)
    return jsonify({"ok": True})


@app.route("/api/items/<int:item_id>", methods=["PUT"])
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


if __name__ == "__main__":
    app.run(debug=True)