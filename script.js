document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();

    // Cattura i dati del modulo
    const titolo = document.querySelector('input[name="titolo"]').value;
    const descrizione = document.querySelector('textarea[name="descrizione"]').value;
    const immagineInput = document.querySelector('input[name="immagine"]');
    const immagine = immagineInput.files.length > 0 ? "img/" + immagineInput.files[0].name : "";

    // Crea l'oggetto JSON
    const nuovoLibro = {
        titolo: titolo,
        descrizione: descrizione,
        immagini: immagine ? [immagine] : []
    };

    // Invia i dati al server
    fetch('/aggiungi-libro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(nuovoLibro)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Errore:', error);
    });
});