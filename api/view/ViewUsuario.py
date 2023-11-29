from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def api_usuario_saudavel():
    return "API-Usuario saudavel"


def view_usuario():
    app.run(host="0.0.0.0", port=5000)
