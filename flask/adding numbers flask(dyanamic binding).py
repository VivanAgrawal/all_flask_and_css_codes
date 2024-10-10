from flask import Flask, request

app = Flask(__name__)


@app.route('/add')
def add_numbers():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')



    result = int(num1) + int(num2)
    return f"The sum of {num1} and {num2} is: {result}"
if __name__ == '__main__':
    app.run()