from flask import Flask, render_template, request, jsonify
import database  # your database.py file

app = Flask(__name__)

# Make sure DB/table exists when app starts
database.createDatabase()

# -------- Pages --------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# -------- API --------

@app.route("/api/items", methods=["GET"])
def api_get_items():
    # Your database.py doesn't have "get all", so we use search("") as a simple workaround
    # BUT your current search uses "=" exact match, so "" won't return everything.
    # If you *do* want all items, easiest is to add a getAllItems() function later.
    #
    # For now, this endpoint will return empty unless you implement "get all".
    return jsonify([])


@app.route("/api/search", methods=["GET"])
def api_search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify([])
    rows = database.search(q)
    # rows are tuples in your database.py, convert to dicts for JSON
    items = []
    for r in rows:
        items.append({
            "ItemID": r[0],
            "Name": r[1],
            "Description": r[2],
            "Category": r[3],
            "Quantity": r[4],
            "Location": r[5],
            "LastUpdated": r[6],
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
