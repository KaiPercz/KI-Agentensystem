📘 Langflow OSS 1.5.xpost1 – Installationsanleitung für Ubuntu 25.04

🔧 Voraussetzungen
- Ubuntu 25.04 (aktuelles System)
- Python 3.13 (wird über uv verwaltet)
- root-Rechte für Systemdienste (systemd)
- Optional: xclip für Secret Key in Zwischenablage

📦 1. Vorbereitungen
1.1 UV installieren (moderne Python-Toolchain)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1.2 Virtuelle Umgebung mit Python 3.13 erstellen
```bash
uv venv --python 3.13
source .venv/bin/activate
```

Stelle sicher, dass deine .env Datei geschützt ist:
```bash
chmod 600 ~/.env
```

📁 2. Verzeichnisse und Services einrichten
2.1 Projektverzeichnisse anlegen
```bash
mkdir -p ~/langflow ~/chroma ~/docs
```

2.2 🧾 systemd-Service langflow.service
🔹 Speicherort
```bash
/etc/systemd/system/langflow.service
```

📄 Inhalt der Datei
```bash
[Unit]
Description=Langflow Backend Service
After=network.target

[Service]
Type=simple
User=kai
WorkingDirectory=/home/kai/langflow
EnvironmentFile=/home/kai/.env
ExecStart=/home/kai/.venv/bin/uv run langflow run --components-path /home/kai/langflow/components/custom/ --env-file /home/kai/.env
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

📘 Erklärung der Abschnitte
🔸 [Unit]
| Eintrag                | Beschreibung                                                                   |
| ---------------------- | ------------------------------------------------------------------------------ |
| `Description`          | Anzeige des Dienstnamens bei `systemctl`                                       |
| `After=network.target` | Dienst startet erst, wenn Netzwerk verfügbar ist (z. B. API-Zugriff notwendig) |


🔸 [Service]
| Eintrag              | Beschreibung                                                                  |
| -------------------- | ----------------------------------------------------------------------------- |
| `Type=simple`        | Standardtyp: der Dienst wird als einfacher Prozess gestartet                  |
| `User=kai`           | Ausführender Benutzer (muss auf deinem System existieren)                     |
| `WorkingDirectory`   | Arbeitsverzeichnis, in dem Langflow-Komponenten und Daten liegen              |
| `EnvironmentFile`    | Verweist auf `.env` mit `LANGFLOW_SECRET_KEY`, API-Schlüsseln etc.            |
| `ExecStart`          | Startbefehl für Langflow – nutzt `uv` und lädt benutzerdefinierte Komponenten |
| `Restart=on-failure` | Neustart bei Abstürzen (nicht bei manuellem Stop)                             |
| `RestartSec=5`       | Wartezeit von 5 Sekunden vor Neustart                                         |
| `StandardOutput`     | Ausgabe geht an `journalctl`                                                  |
| `StandardError`      | Fehlerausgaben ebenso                                                         |

🔸 [Install]
| Eintrag                      | Beschreibung                                                |
| ---------------------------- | ----------------------------------------------------------- |
| `WantedBy=multi-user.target` | Dienst wird beim Systemstart im Mehrbenutzermodus aktiviert |

🧪 Verwaltung des Dienstes
Dienst aktivieren (automatisch beim Booten starten)
```bash
sudo systemctl enable langflow.service
```

Dienst starten
```bash
sudo systemctl start langflow.service
```

Dienst stoppen
```bash
sudo systemctl stop langflow.service
```

Dienststatus anzeigen
```bash
systemctl status langflow.service
```

Echtzeit-Logausgabe anzeigen
```bash
journalctl -u langflow.service -f
```

🛠️ Tipps bei Fehlern
- Berechtigungen prüfen: .env sollte chmod 600 haben, lesbar für User=kai.
- Pfade prüfen: ExecStart, EnvironmentFile, WorkingDirectory – alle Pfade müssen korrekt gesetzt sein.
- Zugriffsrechte auf .venv und Langflow-Verzeichnis: sicherstellen, dass der Nutzer kai Zugriff hat.

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

🔨 3. Abhängigkeiten installieren
```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev gcc
```

📥 4. Langflow installieren

```bash
source /home/kai/.venv/bin/activate
```

4.1 Normale Installation
```bash
uv pip install langflow
```

4.2 Pip aktualisieren
```bash
pip install --upgrade pip
```

4.3 Version prüfen
```bash
pip freeze | grep langflow
```

🔐 5. Umgebungsvariablen setzen
Erzeuge und kopiere den Secret Key:
```bash
python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | xclip -selection clipboard
```

Beispiel .env Datei:
```bash
LANGFLOW_SECRET_KEY=PKKMg...ufDDqavYJM5XSU
OPENAI_API_KEY=sk-l5Kn...ZUEgslrtf_Y
LANGFLOW_API_KEY=IIR-gVTo...5-B--
```

Speichern als ~/.env (ggf. Pfade anpassen) und schützen:
```bash
chmod 600 ~/.env
```

🏁 6. Starten von Langflow

6.1 Manuell (z. B. für Test oder Debugging)
```bash
source ~/.venv/bin/activate
uv run langflow run --components-path langflow/components/custom/ --env-file ~/.env
```

6.2 Automatisch (als systemd-Service)
```bash
sudo systemctl start langflow.service
```

6.3 Status prüfen
```bash
systemctl status langflow.service
```

🌐 7. Zugriff
Nach erfolgreichem Start erreichst du Langflow unter:
```bash
http://127.0.0.1:7860
```

🛑 Langflow stoppen
Wenn du Langflow manuell gestartet hast:
```bash
Ctrl+C    # zum Stoppen
deactivate  # um die virtuelle Umgebung zu verlassen
```

📎 Hinweise
- Komponentenverzeichnis: langflow/components/custom/
- Bei Problemen: Log-Ausgaben mit journalctl -u langflow.service -f prüfen.
