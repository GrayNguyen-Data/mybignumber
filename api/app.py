from flask import Flask, request, jsonify
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mybignumber import MyBigNumber

app = Flask(__name__)
bn = MyBigNumber()

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    if not data or "num1" not in data or "num2" not in data:
        return jsonify({"success": False, "error": "num1 and num2 are required"})

    num1 = str(data["num1"])
    num2 = str(data["num2"])
    result = bn.sum(num1, num2)

    return jsonify({"num1": num1, "num2": num2, "result": result, "success": True})


@app.route('/add_get', methods=['GET'])
def add_numbers_get():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if not num1 or not num2:
        return jsonify({"success": False, "error": "num1 and num2 are required"})

    result = bn.sum(str(num1), str(num2))
    return jsonify({"num1": num1, "num2": num2, "result": result, "success": True})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
