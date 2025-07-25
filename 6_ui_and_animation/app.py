from flask import Flask, send_from_directory, json

app = Flask(__name__, static_folder="static")

customers = [
    {
        "id": 1, 
        "joined": '2000-12-02', 
        "name":'John', 
        "city":'Chandler', 
        "orderTotal": 9.9956,
        "orders": [
            {
                "id": 1,
                "product": 'Shoes',
                "total": 9.9956
            }
        ]
    }, 
    {
        "id": 2, 
        "joined": '1965-01-25',
        "name":'Zed', 
        "city":'Las Vegas', 
        "orderTotal": 19.99,
        "orders": [
            {
                "id": 2,
                "product": 'Baseball',
                "total": 9.995
            },
            {
                "id": 3,
                "product": 'Bat',
                "total": 9.995
            }
        ]
    },
    {
        "id": 3, 
        "joined": '1944-06-15',
        "name":'Tina', 
        "city":'New York', 
        "orderTotal":44.99,
        "orders": [
            {
                "id": 4,
                "product": 'Headphones',
                "total": 44.99
            }
        ]
    }, 
    {
        "id": 4, 
        "joined": '1995-03-28',
        "name":'Dave', 
        "city":'Seattle', 
        "orderTotal":101.50,
        "orders": [
            {
                "id": 5,
                "product": 'Kindle',
                "total": 101.50
            }
        ]
    }
]

# Serve the AngularJS app
@app.route("/")
def serve_angular():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("static", path)

@app.route("/customers")
def customers_data():
    return json.jsonify(customers)

@app.route("/orders")
def orders_data():
    orders = []
    for c in customers:
        orders += c["orders"]
    return json.jsonify(orders)

@app.route("/customers/<customer_id>")
def customer_data(customer_id):
    customer = [c for c in customers if c["id"] == int(customer_id)][0]
    return json.jsonify(customer)

@app.errorhandler(404)
def not_found(e):
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
