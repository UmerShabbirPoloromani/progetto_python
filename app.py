from flask import Flask, request, render_template, redirect, url_for
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