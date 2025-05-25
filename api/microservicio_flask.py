from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
clf = joblib.load("modelo/modelo_inferencia.pkl")
vectorizer = joblib.load("modelo/vectorizador.pkl")

@app.route("/inferir", methods=["POST"])
def inferir():
    texto = request.json.get("texto", "")
    vect = vectorizer.transform([texto])
    pred = clf.predict(vect)[0]
    return jsonify({"nivel": int(pred)})

if __name__ == "__main__":
    app.run(port=5000)
