from flask import Flask, request, render_template
from bs4 import BeautifulSoup  # Per modificare l'HTML

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("paginaPrincipale.html")

@app.route("/aggiungi_paragrafo", methods=["POST"])
def aggiungi_paragrafo():
    
    # Modifica il file HTML
    with open("templates/paginaPrincipale.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    # Aggiungi il nuovo paragrafo al body
    nuovo_elemento = soup.new_tag("p")
    nuovo_elemento.string = "nuovo_paragrafo"
    soup.body.append(nuovo_elemento)
    
    # Salva le modifiche al file HTML
    with open("templates/paginaPrincipale.html", "w", encoding="utf-8") as file:
        file.write(str(soup))
    
    return "Paragrafo aggiunto con successo!"

if __name__ == "__main__":
    app.run(debug=True)