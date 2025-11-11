from flask import Flask, request, jsonify
import calc

app = Flask(__name__)


@app.route('/calc', methods=['GET'])
def calcular():
    op = request.args.get("op")
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 1))

    try:
        if op == "suma":
            result = calc.suma(a, b)
        elif op == "resta":
            result = calc.resta(a, b)
        elif op == "multiplicar":
            result = calc.multiplicar(a, b)
        elif op == "dividir":
            result = calc.dividir(a, b)
        else:
            return jsonify(error="Operación inválida"), 400

        return jsonify(resultado=result)

    except Exception as e:
        return jsonify(error=str(e)), 400


@app.route("/")
def home():
    return "Calculadora Web activa"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
