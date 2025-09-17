from flask import Flask 
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, API World!"




@app.route("/about")
def about():
    return "This is my first API!"

@app.route("/info")
def info():
    return jsonify({
        "Name" : "Andy",
        "Age" : 24,
        "Location" : "Queens,NY"
    })

@app.route("/greet/<name>")
def greet(name):
    return jsonify({
        "message" : f"Hello,{name}"
    })


@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    result = data["a"] + data["b"]
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)