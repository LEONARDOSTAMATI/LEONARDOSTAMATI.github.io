# Configurazione RSVP con Google Sheets

Segui questa guida per collegare il tuo form RSVP a Google Sheets e ricevere le email.

## 1. Crea il Foglio Google
1. Vai su [Google Sheets](https://sheets.google.com) e crea un nuovo foglio vuoto.
2. Chiamalo `Matrimonio RSVP`.
3. Nella **prima riga** (intestazione), scrivi esattamente questi titoli nelle colonne da A a N:
   - **A**: Data Invio
   - **B**: Email (ID Univoco)
   - **C**: Nome e Cognome
   - **D**: Matrimonio (12-09)
   - **E**: Welcome Party (11-09)
   - **F**: Adulti
   - **G**: Bambini
   - **H**: Preferenze Alimentari
   - **I**: Note/Allergie
   - **J**: Pernottamento
   - **K**: Data Arrivo
   - **L**: Data Partenza
   - **M**: Culle
   - **N**: Provenienza (Sito)

## 2. Crea lo Script
1. Nel foglio, clicca su **Estensioni** > **Apps Script**.
2. Si aprirà un editor. Cancella tutto il codice presente.
3. Incolla il seguente codice:

```javascript
/* 
  Back-end RSVP per Matrimonio Andrea & Leonardo 
  -----------------------------------------------
  - Salva i dati su Google Sheet
  - Controlla duplicati (basato su email)
  - Invia notifica email a te 
*/

// CONFIGURAZIONE
const EMAIL_NOTIFICHE = "leonardostamati@gmail.com"; 
const SHEET_NAME = "Foglio1"; // Se hai rinominato il foglio in basso, cambialo qui

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000); // Aspetta max 10s per evitare sovrascritture

  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    
    // Leggi i parametri inviati dal sito
    // Il sito invierà i dati come stringa JSON nel corpo della richiesta
    const data = JSON.parse(e.postData.contents);
    
    const email = data.email.toString().trim().toLowerCase();
    
    // 1. CONTROLLO DUPLICATI
    // Controlliamo la colonna B (indice 1)
    const values = sheet.getDataRange().getValues();
    for (let i = 1; i < values.length; i++) {
        if (values[i][1].toString().trim().toLowerCase() == email) {
            return responseJSON({ 
                result: "error", 
                message: "Esiste già una risposta con questa email!" 
            });
        }
    }

    // 2. SALVATAGGIO DATI
    // Mappa i dati del form alle colonne (A=0, B=1, etc.)
    const timestamp = new Date();
    const row = [
      timestamp,                          // A: Data Invio
      email,                              // B: Email (ID Univoco)
      data.nome,                          // C: Nome e Cognome
      data["presenza-matrimonio"] || "",  // D: Matrimonio (12-09)
      data["presenza-welcome"] || "",     // E: Welcome Party (11-09)
      data.ospiti || "0",                 // F: Adulti
      data.bambini || "0",                // G: Bambini
      data.dieta || "",                   // H: Preferenze Alimentari
      data.note || "",                    // I: Note/Allergie
      data.pernottamento || "no",         // J: Pernottamento
      data.arrivo || "",                  // K: Data Arrivo
      data.partenza || "",                // L: Data Partenza
      data.culla || "0",                  // M: Culle
      data["sito-provenienza"] || ""      // N: Provenienza
    ];

    sheet.appendRow(row);

    // 3. INVIO EMAIL DI NOTIFICA
    try {
      MailApp.sendEmail({
        to: EMAIL_NOTIFICHE,
        subject: "Nuovo RSVP: " + data.nome,
        htmlBody: `
          <h2>Nuova conferma ricevuta! 💍</h2>
          <p><strong>Nome:</strong> ${data.nome}</p>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Matrimonio (12-09):</strong> ${data["presenza-matrimonio"] || "Non specificato"}</p>
          <p><strong>Welcome Party (11-09):</strong> ${data["presenza-welcome"] || "Non specificato"}</p>
          <p><strong>Ospiti:</strong> ${data.ospiti || 0} adulti, ${data.bambini || 0} bambini</p>
          <p><strong>Preferenze alimentari:</strong> ${data.dieta || "Nessuna"}</p>
          <p><strong>Pernottamento:</strong> ${data.pernottamento || "no"}</p>
          <p><strong>Date soggiorno:</strong> ${data.arrivo || "N/A"} → ${data.partenza || "N/A"}</p>
          <p><strong>Culle:</strong> ${data.culla || 0}</p>
          <p><strong>Note:</strong> ${data.note || "Nessuna"}</p>
          <p><strong>Provenienza Sito:</strong> ${data["sito-provenienza"] || "N/A"}</p>
          <hr>
          <p><a href="${SpreadsheetApp.getActiveSpreadsheet().getUrl()}">Apri il Foglio Google</a></p>
        `
      });
    } catch (err) {
      console.log("Errore invio mail: " + err);
      // Non blocchiamo il salvataggio se la mail fallisce
    }

    return responseJSON({ result: "success" });

  } catch (e) {
    return responseJSON({ result: "error", message: e.toString() });
  } finally {
    lock.releaseLock();
  }
}

// Helper per formattare la risposta JSON (CORRETTO per CORS)
function responseJSON(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
```

4. Premi l'icona del floppy disk 💾 per salvare. Dai un nome al progetto (es. "WeddingScript").

## 3. Pubblica (Deploy)
**Passaggio CRITICO. Segui attentamente:**

1. Clicca sul pulsante blu **Esegui il deployment** (in alto a destra) > **Nuovo deployment**.
2. Clicca sull'ingranaggio ⚙️ accanto a "Seleziona tipo" > scegli **Applicazione web**.
3. Compila così:
   - **Descrizione**: _v1_
   - **Esegui come**: `Utente: io` (la tua mail)
   - **Chi può accedere**: `Chiunque` (Importante! Se metti "Solo io" il sito non funzionerà).
4. Clicca **Esegui il deployment**.
5. Google ti chiederà di autorizzare lo script (per accedere a Fogli e Mail).
   - Clicca *Autorizza accesso*.
   - Se esce "App non verificata" -> Clicca **Avanzate** -> **Apri WeddingScript (non sicuro)** -> **Consenti**.
6. Copia l'**URL applicazione web** (finisce con `/exec`).

## 4. Inserisci l'URL nel sito
1. Apri il file `index4.html` del tuo sito.
2. Cerca la variabile `SCRIPT_URL` (la troverai verso la fine, nel codice che sto per aggiungere).
3. Incolla il link tra le virgolette.
4. Salva e carica il sito su GitHub.
