# A REST API returns inconsistent errors to the client. How would you redesign the endpoint behavior?​

# @app.route("/orders/<order_id>")​
# def get_order(order_id):​
# order = db.get(order_id)​
# return order​

# ------------------------------------
# create flask API endpoint to retrieve order details by order_id
# get the order ID from the URL
# check the order in the data
# return 404 if not found
# return 200 if found and 500 if there is an internal server error

import logging
from flask import Flask
app = Flask(__name__)
orders = {
    "1": {"id": "1", "item": "Laptop", "quantity": 1},
    "2": {"id": "2", "item": "Phone", "quantity": 2},
}
@app.route("/orders/<order_id>")
def get_order(order_id):
    try:
        order = orders.get(order_id)
        if order is None:
            return {"error": "Order not found"}, 404
        return order, 200
    except Exception as e:
        logging.error(f"Error retrieving order {order_id}: {e}")
        return {"error": "Internal server error"}, 500
if __name__ == "__main__":
    app.run(debug=True)        
