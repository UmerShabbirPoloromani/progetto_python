from bs4 import BeautifulSoup  # Per modificare l'HTML
import json, os, random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def pagina_principale():
    return render_template('paginaPrincipale.html')

@app.route('/aggiorna', methods=['POST'])
def aggiorna():
    # Quando si clicca sul bottone, si reindirizza alla pagina aggiornata
    nuovo_testo = "Il contenuto del paragrafo è stato aggiornato!"
    return render_template('paginaAggiornata.html', paragrafo=nuovo_testo)

if __name__ == '__main__':
    app.run(debug=True)