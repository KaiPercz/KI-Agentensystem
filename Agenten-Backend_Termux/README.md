# 📘 Agenten-Backend mit LangChain und FastAPI (Termux-kompatibel)

Dieses Projekt verfolgt das Ziel, ein **modulares Agentensystem** auf Basis von **LangChain**, **FastAPI** und optionalem **MQTT**/Speicher aufzubauen. Es läuft auf einem Android-Gerät via **Termux**, ist leichtgewichtig, aber ausbaufähig hin zu einem verteilten System mit autonomen Agenten.

---

## 🚀 Zielsetzung

Ein lokal lauffähiges Backend, das:

- Anfragen an einen KI-Agenten über HTTP erlaubt
- Werkzeuge ("Tools") zur Informationsbeschaffung, Berechnung etc. nutzt
- Mit Gedächtnis arbeitet, um Kontexte zu erkennen
- Mehrere Agentenrollen und ein Event-basiertes System integrieren kann
- Sitzungsbasiert pro Nutzer interagiert (UUID)
- Dialogverläufe speicherbar und ladbar macht

---

## 📦 Architekturübersicht

```text
[Client / CURL / App / Browser]
        |
    [FastAPI REST-Backend]
        |
    [LangChain Agent pro Session/UUID]
        |
  +-----+------+----------------+
  |            |                |
[Memory]    [LLM]           [Tools]
                |                |
        (OpenAI oder      [Search, Math, etc.]
        lokales Modell)
```

---

## 🧩 Implementierte Phasen

### ✅ Phase 1: Minimaler `/ask` Endpoint

* HTTP POST `/ask`
* OpenAI LLM gibt Antwort auf Anfrage
* Kein Kontext oder Tools

### ✅ Phase 2: Tools (Rechner + Websuche)

* Integration von `LLMMathChain` und `DuckDuckGoSearch`
* Agent-Typ: `ZERO_SHOT_REACT_DESCRIPTION`

### ✅ Phase 3: Gedächtnis (Memory)

* Nutzung von `ConversationBufferMemory`
* Agent-Typ: `CONVERSATIONAL_REACT_DESCRIPTION`
* Versteht Bezüge innerhalb einer Session

### ✅ Phase 3b: Sitzungsverwaltung (NEU)
- Mehrere Nutzer/Sitzungen über UUID
- Separate Agenten/Memories je Sitzung
- Dialogverlauf als JSON-Datei speicher- und ladbar

---

## 🔜 Geplante Erweiterungen

### 🧭 Phase 4: Agentenrollen & Event-System

* Verschiedene Agententypen (z. B. Planer, Ausführer, Speicher)
* Kommunikation über Ereignisse (MQTT/TCP)
* Modularisierung pro Agentenkomponente

### 📊 Phase 5: GUI

* Web-Interface oder Telegram-Frontend
* Visualisierung der Agentenkommunikation

---

## ⚙️ Voraussetzungen

* Termux
* Python 3.10+
* Pakete:

  * fastapi
  * uvicorn
  * langchain
  * openai
  * duckduckgo-search

---

## ▶️ Installation und Start in Termux

### 1. Termux vorbereiten

```bash
pkg update && pkg upgrade
pkg install -y \
  python \
  clang \
  libffi \
  openssl \
  openssl-tool \
  libjpeg-turbo \
  python-pip \
  freetype \
  pkg-config \
  python-numpy \
  libcrypt \
  git

```

### 2. Repository klonen (bzw. Projektstruktur kopieren)

```bash
git clone https://github.com/KaiPercz/KI-Agentensystem.git
cd KI-Agentensystem
cd Agenten-Backend_Termux
```

### 3. Abhängigkeiten installieren
je nach verwendeten Modell wird das eine ganze Zeit (> 3 Stunden) benötigen...

```bash
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

### 4. OpenAI API Key setzen 

z.B. temporär:
```bash
export OPENAI_API_KEY=sk-...
```

oder in der .env Datei:
```bash
OPENAI_API_KEY=sk-...
```

### 5. Server starten

```bash
uvicorn main:app --host 0.0.0.0 --port 7860
```

Du kannst nun per HTTP auf den Agenten zugreifen:

```bash
curl -X POST http://localhost:7860/ask -H "Content-Type: application/json" -d '{"question": "Wie funktioniert das Periodensystem?", "session_id": "kai123"}'
```

---

## 📁 Projektstruktur (aktuell)

```text
Agenten-Backend_Termux/
├── main.py           # FastAPI-App mit Agentenlogik
├── requirements.txt  # Paketliste
├── README.md         # Projektdokumentation
├── sessions/         # Sitzungsbezogene JSON-Dateien
```

---

## ✍️ Pflegehinweis

Diese Datei wird mit jeder Entwicklungsphase erweitert, um Struktur, Zielbild und aktuelle Implementierung stets nachvollziehbar zu dokumentieren.

---

Letzter Stand: Unterstützung für mehrere Nutzer/Sitzungen (UUID-basiert) und speicherbare Dialogverläufe als JSON.

