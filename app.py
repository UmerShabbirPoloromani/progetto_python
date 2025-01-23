from flask import Flask, request, render_template
from bs4 import BeautifulSoup  # Per modificare l'HTML
import json, os, random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
   
    return render_template("paginaPrincipale.html")

@app.route("/inserisci")
def inserisci():
    return render_template("caricaLibro.html")


if __name__ == "__main__":
    app.run(debug=True)