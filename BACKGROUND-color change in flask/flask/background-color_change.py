from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def magic_color():
    return render_template('index.html')

@app.route('/get_color')
def get_color():
    colors = ['#FF5733', '#33FF57', '#5733FF', '#FF33A3', '#33A3FF']
    random_color = random.choice(colors)
    return random_color

if __name__ == '__main__':
    app.run(debug=True)