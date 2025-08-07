# 🧠 Node-RED Flow: Vorqualifizierung und dynamischer Agentenaufruf

## Übersicht

Dieser Flow verarbeitet strukturierte Inhalte aus E-Mails nach der Vorqualifizierung und entscheidet anhand des Klassifikations-Ergebnisses, welcher spezialisierte Agent (z. B. Reiseagent, Finanzagent etc.) aufgerufen wird. Der Flow beinhaltet HTTP-Rückmeldung, Session-ID-Verarbeitung, Fehlerbehandlung sowie strukturierte Protokollierung.

---

## 🌐 Architekturübersicht

```plaintext
[Vorqualifizierung (Input)]
    ↓
[Antwort Vorqualifizierung]
    ├──→ [Set HTTP 200]
    ↓
[Session ID ermitteln]
    ↓
[Agentenaufruf]
    ├─→ [Reiseagent]
    ├─→ [Finanzwelt]
    ├─→ [sonstiges]
    └─→ [ein Problem]

Parallel:
[Agentenaufruf] → [Daten generieren] → [Protokoll DB] → [http request] → [Fehler abfangen]
                                                ↓                ↓
                                       [Fehlermeldung generieren] / [Daten generieren]
                                                           ↓
                                                    [Protokoll DB]
                                                           ↓
                                      [Serverantwort Langflow Reiseagent]
```


📌 Komponentenbeschreibung
| Komponente                                            | Funktion                                                                    |
| ----------------------------------------------------- | --------------------------------------------------------------------------- |
| **Vorqualifizierung**                                 | Eingang des Flows mit klassifizierten Daten aus der Mailverarbeitung.       |
| **Antwort Vorqualifizierung**                         | Optionaler Rückkanal an vorigen Flow oder Auslöser.                         |
| **Set HTTP 200**                                      | Bestätigung, dass die Anfrage verarbeitet wurde.                            |
| **Session ID ermitteln**                              | Extrahiert oder erzeugt eine eindeutige Session-ID für Nachverfolgbarkeit.  |
| **Agentenaufruf**                                     | Zentrale Steuerung: Wählt den zuständigen Agenten basierend auf Kategorie.  |
| **Reiseagent / Finanzwelt / sonstiges / ein Problem** | Jeweils zuständige Knoten zur Weiterverarbeitung je nach Kontext.           |
| **Daten generieren**                                  | Strukturierte Datenerzeugung für Logging und API-Übergabe.                  |
| **Protokoll DB**                                      | Logging-Schritt zur zentralen Protokollierung (z. B. via SQLite).           |
| **http request**                                      | Übergibt Daten an z. B. einen Langflow-Agenten via HTTP-API.                |
| **Fehler abfangen**                                   | Reaktion auf API-Fehler oder unerwartete Antworten.                         |
| **Fehlermeldung generieren**                          | Erstellt lesbare Fehlerobjekte.                                             |
| **Serverantwort Langflow Reiseagent**                 | Zielknoten für Output aus dem Prozess oder Rückkanal zur UI.                |


✅ Prozessschritte
1. Input: Vorqualifizierte Daten treffen am Startpunkt ein.
2. Antwort optional: Ein HTTP 200-OK wird zurückgegeben.
3. Session-Tracking: Die Session-ID wird extrahiert oder generiert.
4. Agentenwahl: Basierend auf der Klassifikation wird der zuständige Agent ausgewählt.
5. Datenübergabe: Der ausgewählte Agent sendet strukturierte Daten zur weiteren Verarbeitung.
6. Logging: Jede Aktion wird in der Protokoll-Datenbank gespeichert.
7. Fehlerbehandlung: Bei Fehlern wird eine Fehlermeldung erzeugt und geloggt.
8. Ergebnis: Der finale Zustand (Erfolg oder Fehler) wird am Ende des Flows bereitgestellt.


📊 Dynamisches Routing (Agentenlogik)
| Klassifikation | Ziel-Agent  |
| -------------- | ----------- |
| `reise`        | Reiseagent  |
| `finanzen`     | Finanzwelt  |
| `unbekannt`    | sonstiges   |
| `problem`      | ein Problem |


📂 Hinweise zur Wartung
- Stelle sicher, dass alle Klassifikationen im Agentenaufruf korrekt behandelt werden.
- Füge ggf. Logging-Mechanismen pro Agent hinzu, um individuelle Pfade nachvollziehen zu können.
- Achte auf Session-ID-Eindeutigkeit, insbesondere bei parallelen Eingängen.
- Teste regelmäßig das Fehlerhandling des http request.


🛠️ Erweiterungsideen (Roadmap)
| Thema                                      | Status     |
| ------------------------------------------ | ---------- |
| Automatisches Training der Klassifizierung | Geplant    |
| Konfiguration über externe JSON-Map        | In Planung |
| Anbindung weiterer Agenten (IoT, Technik)  | Offen      |
| Session-Tracking über Redis                | erledigt   |


📎 Anhang
Diese Dokumentation basiert auf einem Node-RED-Flow zur intelligenten Weiterleitung klassifizierter Daten an Agentenprozesse, inklusive Logging, Fehlerbehandlung und Session-Management (Stand: August 2025).


