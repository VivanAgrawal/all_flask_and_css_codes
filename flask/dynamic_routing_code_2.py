from flask import Flask

app = Flask(__name__)

# A dictionary to store book details by their IDs
items = {
    'apple': {'name': 'Apple', 'price': 0.5},
    'banana': {'name': 'Banana', 'price': 0.25},
    'orange': {'name': 'Orange', 'price': 0.75},
}

@app.route('/')
def home():
    return "Welcome to our itemstore!"

@app.route('/items/<item_id>')
def item_details(item_id):
    if item_id in items:
        item = items[item_id]
        name = item['name']
        price = item['price']
        return f"Displaying details for item {item_id}: {name} price {price}"
    else:
        return "item not found"

if __name__ == '__main__':
    app.run()