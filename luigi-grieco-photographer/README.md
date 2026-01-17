# Portfolio Luigi Grieco - Fotografo

Sito web portfolio minimal ed elegante per il fotografo Luigi Grieco.

## Caratteristiche

- Design minimal ed elegante con palette grigia/scura
- Animazioni fluide e interattive
- Sistema di tab per organizzare le foto per categoria
- Responsive design per tutti i dispositivi
- Cursor personalizzato
- Modal per visualizzazione immagini

## Struttura del Progetto

```
luigi-grieco-portfolio/
├── index.html          # Pagina principale
├── styles.css          # Stili CSS
├── script.js           # JavaScript per animazioni e interattività
├── README.md           # Questo file
└── .nojekyll           # File per GitHub Pages (se necessario)
```

## Deploy su GitHub Pages come Sottodominio

### Opzione 1: Repository dedicato (Consigliato)

1. **Crea un nuovo repository su GitHub** chiamato `luigi-grieco-portfolio` (o il nome che preferisci)

2. **Inizializza Git nel progetto locale:**
   ```bash
   cd luigi-grieco-portfolio
   git init
   git add .
   git commit -m "Initial commit - Portfolio Luigi Grieco"
   ```

3. **Collega il repository remoto:**
   ```bash
   git remote add origin https://github.com/TUO_USERNAME/luigi-grieco-portfolio.git
   git branch -M main
   git push -u origin main
   ```

4. **Attiva GitHub Pages:**
   - Vai su GitHub → Settings → Pages
   - Sotto "Source", seleziona il branch `main` e la cartella `/ (root)`
   - Clicca "Save"

5. **Configura il sottodominio:**
   - Il sito sarà disponibile su: `https://TUO_USERNAME.github.io/luigi-grieco-portfolio/`
   - Per usare un sottodominio personalizzato (es. `luigi.tuodominio.com`):
     - Crea un file `CNAME` nella root del repository con il dominio
     - Configura il DNS del tuo dominio per puntare a GitHub Pages

### Opzione 2: Sottodominio del tuo GitHub Pages principale

Se vuoi usare un sottodominio del tuo GitHub Pages principale (es. `luigi.tuonome.github.io`):

1. **Crea un file `CNAME`** nella root del repository con il contenuto:
   ```
   luigi.tuonome.github.io
   ```

2. **Oppure configura il DNS** per puntare un sottodominio del tuo dominio principale a GitHub Pages

## Personalizzazione

### Sostituire le immagini placeholder

Le immagini attualmente usano un servizio placeholder. Per sostituirle con foto reali:

1. Crea una cartella `images/` nel progetto
2. Aggiungi le tue foto con nomi descrittivi
3. Modifica `script.js` nella sezione del modal per usare i percorsi corretti:
   ```javascript
   modalImage.src = `images/ritratto-${imageNumber}.jpg`;
   ```

### Modificare i testi

Tutti i testi sono nel file `index.html`. Puoi modificare:
- La descrizione nella sezione "Chi Sono"
- I titoli delle categorie nei tab
- Le informazioni di contatto

### Personalizzare i colori

I colori sono definiti come variabili CSS in `styles.css`:
```css
:root {
    --bg-primary: #0a0a0a;
    --bg-secondary: #1a1a1a;
    --text-primary: #e0e0e0;
    --accent: #ffffff;
    /* ... */
}
```

## Browser Supportati

- Chrome (ultime 2 versioni)
- Firefox (ultime 2 versioni)
- Safari (ultime 2 versioni)
- Edge (ultime 2 versioni)

## Note

- Il sito è completamente statico e non richiede un server backend
- Le animazioni utilizzano CSS e JavaScript vanilla per prestazioni ottimali
- Il design è responsive e si adatta a tutti i dispositivi

## Licenza

© 2024 Luigi Grieco. Tutti i diritti riservati.

