import random
from flask import Flask, render_template

app = Flask(__name__)

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
]

@app.route('/')
def index():
    # Select a random quote from the list
    random_quote = random.choice(quotes)
    
    data = {'name': 'John', 'age': 30, 'quote': random_quote}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
