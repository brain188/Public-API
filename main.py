from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email" : "tendongnkengafac@gmail.com",
        "current_datetime" : datetime.utcnow().isoformat() + "Z",
        "github_url" :"https://github.com/brain188/Public-API.git"
    }
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


