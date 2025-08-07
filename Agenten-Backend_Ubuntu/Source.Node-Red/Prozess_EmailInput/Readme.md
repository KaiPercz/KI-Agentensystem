# 📧 Node-RED Flow: Automatisierte E-Mail-Verarbeitung mit Vorqualifizierung

## Übersicht

Dieser Node-RED-Flow verarbeitet eingehende E-Mails automatisiert. Ziel ist es, strukturierte Daten aus E-Mails zu extrahieren, diese vorzubereiten (Vorqualifizierung) und an ein externes System wie Langflow zu übergeben. Der Prozess umfasst Logging, Fehlerbehandlung und Rückmeldungen an den Absender/Client.

---

## 🌐 Architekturübersicht

```plaintext
[EMail Input] 
    ↓
[Aufgeschlüsselte Email]
    ├──→ [Set HTTP 200] → [Rückgabewert]
    ↓
[Zuordnung]
    ↓
[Vorqualifizierung] → [http request] → [EMail Inhalt]
                              ↓
                         [Fehler abfangen] ─┬─→ [Fehlermeldung generieren]
                                           └─→ [Daten generieren]
                                                    ↓
                                               [Protokoll DB]
                                                    ↓
                            [Serverantwort Langflow Vorqualifizierung]
```

📌 Komponentenbeschreibung

| Komponente                   | Funktion                                                          |
| ---------------------------- | ----------------------------------------------------------------- |
| **EMail Input**              | Einstiegspunkt für eingehende E-Mails (z. B. über IMAP oder API). |
| **Aufgeschlüsselte Email**   | Verarbeitung, ggf. Entschlüsselung oder MIME-Dekodierung.         |
| **Set HTTP 200**             | Rückmeldung mit HTTP-Status `200 OK` an den Client oder Absender. |
| **Rückgabewert**             | Beendet die Kommunikation mit Rückmeldung.                        |
| **Zuordnung**                | Identifiziert Nachrichtentyp, Zielsystem oder Datenkontext.       |
| **Daten generieren**         | Extrahiert strukturierte Daten aus dem E-Mail-Inhalt.             |
| **Vorqualifizierung**        | Prüft Inhalt auf Relevanz, Kategorie oder Routing-Entscheidung.   |
| **http request**             | Übergibt die Daten an z. B. einen Langflow-Agent per API-Call.    |
| **EMail Inhalt**             | Optional: Anzeige, Logging oder Speicherung des Inhalts.          |
| **Fehler abfangen**          | Erfasst Fehler beim externen API-Aufruf.                          |
| **Fehlermeldung generieren** | Erstellt eine menschlich lesbare Beschreibung des Fehlers.        |
| **Protokoll DB**             | Logging aller Schritte und Ergebnisse in eine Datenbank.          |
| **Serverantwort ...**        | Rückgabe des Prozessergebnisses, inkl. Erfolg oder Fehlerbericht. |


✅ Prozessschritte
1. Eingang: Eine E-Mail trifft ein und wird verarbeitet.
2. Entschlüsselung/Dekodierung erfolgt über die Aufgeschlüsselte Email-Funktion.
3. HTTP 200 Rückgabe erfolgt optional parallel zur Hauptverarbeitung.
4. Zuordnung definiert, wie mit der Mail weiter verfahren wird.
5. Vorqualifizierung entscheidet, ob die Mail relevant ist.
6. Daten werden generiert und an einen Langflow-Agent geschickt (http request).
7. Fehlerbehandlung sorgt bei API-Fehlern für Logging und alternative Datenerzeugung.
8. Protokollierung aller Aktionen und Ergebnisse.
9. Ergebnisübermittlung an einen nachfolgenden Prozess oder eine Statusanzeige.

🛠️ Erweiterungsideen (Roadmap)

| Thema                                         | Status               |
| --------------------------------------------- | -------------------- |
| Signierte/verschlüsselte E-Mails (PGP/S-MIME) | In Planung           |
| Mehrsprachige Zeichensatz-Erkennung           | Geplant              |
| ZIP-Extraktion und Virenscan (ClamAV)         | In Prüfung           |
| E-Mail-Thread-Verfolgung (Thread-ID)          | Teilweise realisiert |
| NLP-Analyse der Inhalte (Langchain)           | Optional             |

🔗 Integration
- Zielsystem (Langflow): Übergabe über http request mit JSON-Payload.
- Protokollierung: Via Protokoll DB-Knoten (z. B. SQLite, InfluxDB oder MongoDB).
- Fehlermanagement: Zentrale Behandlung über gemeinsamen Pfad inkl. Logging.

📂 Hinweise zur Wartung
- Prüfe regelmäßig den http request-Knoten auf Timeouts und Fehler-Codes.
- Sichere die Protokoll DB regelmäßig.
- Nutze Node-RED-Projektfunktionen zur Versionierung des Flows.
