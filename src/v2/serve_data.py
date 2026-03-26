from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/to_do/<rpi_id>")
def to_do(rpi_id:str=""):
    return jsonify({
        "command": "status",
        "return": "results",
        #"value": 42
    })


@app.route("/results", methods=("GET", "POST",))
def results():
    for key in request.values:
        print(key, request.values[key])

    return "OK"




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
