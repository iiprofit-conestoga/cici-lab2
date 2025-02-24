from flask import Flask, jsonify

app = Flask(__name__)

# This is test comment

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Calculator API"})

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return jsonify({"result": num1 + num2})

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return jsonify({"result": num1 - num2})

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return jsonify({"result": num1 * num2})

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    if num2 == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    return jsonify({"result": num1 / num2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 