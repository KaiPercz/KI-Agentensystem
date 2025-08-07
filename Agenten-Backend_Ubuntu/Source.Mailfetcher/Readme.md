# E-Mail-Abruf und Weiterverarbeitung mit Fetchmail und Procmail

Dieses Setup richtet ein automatisiertes System auf einer Ubuntu 24.x Umgebung ein, das E-Mails über `fetchmail` von einem IMAP-Server (z. B. IONOS) verschlüsselt abruft und zur lokalen Weiterverarbeitung an `procmail` übergibt.

Zusätzlich werden Logdateien erstellt und über `logrotate` verwaltet.

---

## 🔧 Installierte Komponenten

| Komponente     | Beschreibung                                                                 |
|----------------|------------------------------------------------------------------------------|
| `fetchmail`    | Holt E-Mails von IMAP/POP3-Servern ab (hier: `imap.ionos.de`)                |
| `procmail`     | Verarbeitet/Filtert eingehende Mails lokal                                   |
| `openssl`      | Ermöglicht manuelle Tests von SSL-Verbindungen                               |
| `ca-certificates` | Ermöglicht die Prüfung von Server-Zertifikaten                            |
| `logrotate`    | Verwalten und Rotieren der Logdateien (`.fetchmail.log`, `procmail.log`)     |

---

## 📁 Angelegte Dateien

| Pfad                            | Beschreibung                                  |
|--------------------------------|-----------------------------------------------|
| `~/.fetchmail.secret`          | Enthält IMAP-Benutzername und Passwort        |
| `~/.fetchmailrc`               | Fetchmail-Konfiguration                       |
| `/etc/logrotate.d/fetchmail-procmail` | Logrotate-Regeln für Mail-Logs             |
| `~/.fetchmail.log`             | Log-Datei für `fetchmail`                    |
| `~/procmail.log`               | Log-Datei für `procmail`                     |

---

## 🛠️ Installationsanleitung

### Voraussetzungen

- Ubuntu 24.04 LTS oder neuer
- Benutzer `fetchmailer` (wird automatisch erstellt, falls nicht vorhanden)
- Zugriff auf IMAP-Daten (Benutzername + Passwort)

---

### Schritt-für-Schritt

1. Skript herunterladen:

    ```bash
    wget https://example.com/setup_fetchmail_ionos.sh -O setup_fetchmail_ionos.sh
    chmod +x setup_fetchmail_ionos.sh
    ```

2. Skript ausführen:

    ```bash
    ./setup_fetchmail_ionos.sh
    ```

3. Zugangsdaten eingeben, wenn das Skript danach fragt.

4. Die Einrichtung erstellt folgende Konfigurationsdateien:

    - `~/.fetchmail.secret` – enthält `benutzer:passwort`
    - `~/.fetchmailrc` – holt E-Mails über SSL von IONOS
    - `/etc/logrotate.d/fetchmail-procmail` – rotiert die Logdateien automatisch

---

## 🔐 Sicherheitshinweise

- Die Datei `~/.fetchmail.secret` enthält **Passwörter im Klartext** und ist daher auf `chmod 600` gesetzt.
- Fetchmail nutzt SSL (`port 993`) mit Zertifikatsprüfung (`sslcertck`).
- Nur der Benutzer `fetchmailer` und `root` dürfen auf die Logdateien zugreifen.

---

## 🚀 Manuelles Starten / Testen

E-Mail-Abruf starten:

```bash
fetchmail -v
```

📬 Weiterverarbeitung mit Procmail
Die Datei ~/.procmailrc kann verwendet werden, um eingehende Mails weiterzuleiten, zu speichern oder zu analysieren.

```bash
LOGFILE=$HOME/procmail.log
VERBOSE=yes
MAILDIR=$HOME/Mail

:0:
* ^Subject:.*Test
testmail
```

🧹 Logrotate-Konfiguration
 - Die Logdateien ~/.fetchmail.log und ~/procmail.log werden täglich rotiert
 - Es werden 5 Generationen aufbewahrt (rotate 5)
 - Alte Logs werden komprimiert (.gz)

🗺️ Roadmap

| Thema                                                       | Beschreibung                                                                                           | Status                             |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| **Signierte/verschlüsselte E-Mails (S/MIME, PGP)**          | Unterstützung für das Verifizieren und Entschlüsseln von E-Mails mit GPG oder S/MIME                   | ⏳ Geplant                          |
| **ZIP-Extraktion und Virenscan (z. B. ClamAV-Integration)** | Automatische Extraktion von ZIP-Anhängen und Prüfung mit ClamAV                                        | ⏳ Geplant                          |
| **Mehrsprachige Charset-Erkennung**                         | Automatische Umwandlung von nicht-UTF-8 Encodings (z. B. ISO-8859-15, Windows-1252)                    | ⏳ Geplant                          |
| **E-Mail-Thread-Verfolgung**                                | Identifikation und Gruppierung zusammengehöriger Konversationen über Message-ID und In-Reply-To Header | ✅ Implementiert (Felder vorhanden) |


📎 Lizenz & Autor
Dieses Skript und die Konfiguration sind als Hilfestellung für den Aufbau eines lokalen Mailverarbeitungssystems unter Linux gedacht. Keine Garantie oder Haftung bei Fehlkonfiguration.

Autor: Kai-Gerd Percz
Stand: 08.2025


