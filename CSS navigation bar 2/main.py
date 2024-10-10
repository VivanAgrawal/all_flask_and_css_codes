from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex1.html')

@app.route('/')
def i():
    return render_template('ex2.html')

@app.route('/')
def ind():
    return render_template('style.css')
if __name__ == '__main__':
    app.run(debug=True)
