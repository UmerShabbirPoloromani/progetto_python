async function submitForm() {
    const form = document.getElementById('book-form');
    const formData = new FormData(form);

    // Creiamo un oggetto JSON dai dati del modulo
    const bookData = {
        titolo: formData.get('titolo'),
        autore: formData.get('autore'),
        descrizione: formData.get('descrizione')
    };
    
    // Invio al server
    const response = await fetch('/add-book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bookData)
    });

    const result = await response.json();
    alert(result.message);
}