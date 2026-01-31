# Generatore di Link Personalizzati

Usa questo metodo per creare velocemente i link per tutti i tuoi invitati.

## Metodo Excel / Google Sheets

1. Inserisci i nomi degli invitati nella colonna **A** (es. A2: `Mario Rossi`).
2. Nella colonna **B**, incolla questa formula:

   **Per Excel (Windows):**
   ```excel
   ="https://leonardostamati.github.io/Andrea-&-Leonardo/index4.html?ospite=" & SOSTITUISCI(A2; " "; "+")
   ```

   **Per Google Sheets / Excel (Mac):**
   ```excel
   ="https://leonardostamati.github.io/Andrea-&-Leonardo/index4.html?ospite=" & ENCODEURL(A2)
   ```

   *(Sostituisci il link base con il tuo dominio reale se diverso o usa localhost per provare)*

3. Trascina la formula giù per tutti gli invitati.
4. Copia la colonna B e invia i link su WhatsApp/Email!

## Esempi

- **Mario Rossi** diventa: `...?ospite=Mario+Rossi`
- **Zio Pino e Zia Maria** diventa: `...?ospite=Zio+Pino+e+Zia+Maria`

## Limite Ospiti (Opzionale)
Puoi limitare il numero di adulti selezionabili aggiungendo `&adulti=N` alla formula.
Esempio (colonna C contiene il numero max adulti):

**Excel (Windows):**
```excel
="https://leonardostamati.github.io/Andrea-&-Leonardo/index4.html?ospite=" & SOSTITUISCI(A2; " "; "+") & "&adulti=" & C2
```

**Google Sheets / Excel (Mac):**
```excel
="https://leonardostamati.github.io/Andrea-&-Leonardo/index4.html?ospite=" & ENCODEURL(A2) & "&adulti=" & C2
```

Se `C2` è 2, il link sarà `...?ospite=...&adulti=2` e il menu mostrerà solo 1 o 2.
