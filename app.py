from flask import Flask, request, render_template, redirect, url_for, flash, render_template, redirect, url_for, jsonify
from bs4 import BeautifulSoup  # Per modificare l'HTML
import json, os, random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("paginaPrincipale.html")

@app.route("/upload", methods=['GET', 'POST'])
def carica():
    return redirect(url_for('home'))


@app.route("/inserisci")
def inserisci():
    return render_template("caricaLibro.html")


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/aggiungi-libro', methods=['POST'])
def aggiungi_libro():
    try:
        data = request.get_json()
        print("Dati ricevuti:", data)  # Log per verificare i dati ricevuti

        json_file = 'libri.json'

        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as file:
                libri = json.load(file)
        else:
            libri = []

        libri.append(data)

        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(libri, file, ensure_ascii=False, indent=4)

        return jsonify({"message": "Libro aggiunto con successo!"}), 200

    except Exception as e:
        print("Errore:", e)
        return jsonify({"message": "Errore durante l'aggiunta del libro"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)