# 01 E-Mail-Verarbeitung mit Bash, Procmail und Langflow-Anbindung

Dieses Skript verarbeitet eingehende E-Mails, extrahiert relevante Inhalte (Absender, Betreff, Body, Anh�nge, Thread ID) und �bertr�gt sie als JSON an eine definierte HTTP-API (z.�B. Langflow). Es ist Teil eines automatisierten Nachrichtensystems.

---

## 02 Zweck

- Empfang eingehender E-Mails �ber `fetchmail` und `procmail`
- Extraktion strukturierter Inhalte aus der E-Mail
- Konvertierung in ein JSON-Dokument
- Filterung von Anh�ngen auf erlaubte MIME-Typen
- Kategorisierung der Anh�nge
- �bergabe an eine externe HTTP-API per `curl` (in diesem Zielbild Langflow)

---

## 03 Verzeichnisstruktur

```text
/home/mailfetcher/
+-- bin/
�   +-- process_email.sh       # Hauptskript zur E-Mail-Verarbeitung
+-- .api_config                # API-Konfiguration (optional)
+-- .procmailrc                # Procmail-Regel zur Skript-Triggerung
+-- .fetchmailrc               # Fetchmail-Parameter zum Abruf der EMails
+-- processing.log             # Laufzeit-Logfile
```

## 04 Ablauf (Prozess�bersicht)
[Mailserver] ? [fetchmail] ? [procmail] ? [process_email.sh] ? [API (Langflow)]

Schritte im Detail:
1. Mailabruf via fetchmail
2. Mailweiterleitung an procmail
3. Pr�fung der Empf�ngeradresse (To: test@ai.percz.de)
4. Aufruf von process_email.sh
5. Extraktion von Header, Body, Anh�ngen
6. MIME-Filterung & Kategorisierung
7. JSON-Erzeugung
8. curl POST an API-Endpunkt


## 05 JSON-Struktur
```text
{
  "from": "absender@example.com",
  "subject": "Testmail",
  "body": "Dies ist der Text der E-Mail",
  "attachments": {
    "pdf": [ { ... } ],
    "images": [ { ... } ],
    "documents": [ { ... } ],
    "other": [ { ... } ],
    "count": 0
  }
}
```

## 06 Konfiguration
```text
.api_config (optional)
API_URL=http://localhost:8080/fallback
LANGFLOW_API_KEY=DEIN_API_KEY
```

## 07 Lizenz
Dieses Skript ist f�r private oder betriebliche Nutzung freigegeben. Keine Garantie auf Vollst�ndigkeit oder Sicherheit.

