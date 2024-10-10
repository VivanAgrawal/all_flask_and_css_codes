import random
from flask import Flask, render_template

app = Flask(__name__)

# List of random numbers
numbers = [1,2,3,4,5,6
]
    

@app.route('/')
def index():
    # Select a random numbers from the list
    random_number = random.choice(numbers)
    
    data = { 'number': random_number}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)