from flask import Flask, request, jsonify
from core import arithmetic

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add_route():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    return jsonify(result=arithmetic.add(a, b))

def run_api():
    app.run(port=5000)
