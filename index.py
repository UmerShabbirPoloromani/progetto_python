from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("paginaPrincipale.html")

@app.route("/process", methods=["POST"])
def process():
    # Recupera i dati inviati dal form
    dato = request.form.get("dato")
    return f"Hai inviato: {dato}"

if __name__ == "__main__":
    app.run(debug=True)