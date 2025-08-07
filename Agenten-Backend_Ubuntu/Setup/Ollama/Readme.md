🧾 Technische Installationsanleitung: Ollama lokal auf Ubuntu 25.04 (ohne Docker)

🔧 Voraussetzungen
| Komponente   | Empfehlung                   |
| ------------ | ---------------------------- |
| OS           | Ubuntu 25.04 (aktuell)       |
| Architektur  | x86\_64 (64-bit)             |
| RAM          | ≥ 8 GB empfohlen             |
| GPU          | Optional, z. B. NVIDIA CUDA  |
| Internet     | Für Download der Modelle     |
| Root-Zugriff | Für systemweite Installation |

📦 1. Installation von Ollama
1.1 Download des Ollama CLI Installers
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

🔒 Hinweis: Das Script lädt eine statische Binary, entpackt sie in /usr/local/bin/ollama und legt ggf. Dienste an.

1.2 Pfad prüfen
```bash
which ollama
```

Erwartete Ausgabe:
/usr/local/bin/ollama

🛠️ 2. Ollama-Dienst starten
Nach der Installation wird der Dienst normalerweise automatisch gestartet.

Dienst manuell starten:
```bash
ollama serve
```

Der Ollama-Server lauscht standardmäßig unter http://localhost:11434.

Dienst im Hintergrund starten (Systemstart)
Service in systemd integrieren, z. B.:

```bash
sudo tee /etc/systemd/system/ollama.service > /dev/null <<EOF
[Unit]
Description=Ollama Server
After=network.target

[Service]
ExecStart=/usr/local/bin/ollama serve
Restart=always
User=kai
Environment=OLLAMA_MODELS=/home/kai/.ollama/models
WorkingDirectory=/home/kai

[Install]
WantedBy=multi-user.target
EOF
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now ollama.service
```

📥 3. Modelldownload und Nutzung

Beispiel: LLaMA 3 herunterladen
```bash
ollama pull llama3
```

Weitere Modelle: https://ollama.com/library

Modell starten:
```bash
ollama run llama3
```

⚙️ 4. Konfiguration (optional)
~/.ollama/config

# ~/.ollama/config
host = "0.0.0.0:11434"
models = "/home/kai/.ollama/models"


🌐 5. Nutzung über REST API

Standardmäßig erreichbar unter: http://localhost:11434

Beispiel: API-Test mit curl

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Was ist eine Enterprise-Architektur?",
  "stream": false
}'
```

📦 6. Update von Ollama
Falls eine neue Version verfügbar ist:

```bash
ollama update
```

🛑 7. Ollama stoppen

```bash
sudo systemctl stop ollama.service
```

Oder bei manuellem Start:

```bash
Ctrl+C
```

📎 Zusammenfassung

| Schritt             | Befehl/Ort                                       |
| ------------------- | ------------------------------------------------ |
| Installation        | `curl -fsSL https://ollama.com/install.sh \| sh` |
| Start (manuell)     | `ollama serve`                                   |
| Start (systemd)     | `sudo systemctl start ollama.service`            |
| Modelle holen       | `ollama pull llama3`                             |
| Start eines Modells | `ollama run llama3`                              |
| API-Nutzung         | `http://localhost:11434`                         |
