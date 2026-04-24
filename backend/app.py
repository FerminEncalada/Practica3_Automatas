from flask import Flask, request, jsonify
from flask_cors import CORS

# AFD
from afd.transacciones import validar_transaccion
from afd.handshake import validar_handshake
from afd.cerradura import validar_cerradura

# AFND
from afnd.genetica import validar_genetica
from afnd.usuario import validar_usuario
from afnd.telemetria import validar_telemetria

app = Flask(__name__)
CORS(app)

# ---------------- AFD ----------------

@app.route("/afd/transacciones", methods=["POST"])
def afd_transacciones():
    cadena = request.json.get("cadena", "")
    return jsonify({"valido": validar_transaccion(cadena)})

@app.route("/afd/handshake", methods=["POST"])
def afd_handshake():
    cadena = request.json.get("cadena", "")
    return jsonify({"valido": validar_handshake(cadena)})

@app.route("/afd/cerradura", methods=["POST"])
def afd_cerradura():
    cadena = request.json.get("cadena", "")
    return jsonify({"valido": validar_cerradura(cadena)})

# ---------------- AFND ----------------

@app.route("/afnd/genetica", methods=["POST"])
def afnd_genetica():
    cadena = request.json.get("cadena", "")
    return jsonify({"valido": validar_genetica(cadena)})

@app.route("/afnd/usuario", methods=["POST"])
def afnd_usuario():
    cadena = request.json.get("cadena", "")
    return jsonify({"valido": validar_usuario(cadena)})

@app.route("/afnd/telemetria", methods=["POST"])
def afnd_telemetria():
    cadena = request.json.get("cadena", "")
    return jsonify({"valido": validar_telemetria(cadena)})

if __name__ == "__main__":
    app.run(debug=True)