# KI-Agentensystem
Entwicklung unterschiedlicher Ansätze von einen Agentensystemen für KI-Anwendungen

a)
# 📘 Agenten-Backend mit LangChain und FastAPI (Termux-kompatibel)

Dieses Projekt verfolgt das Ziel, ein **modulares Agentensystem** auf Basis von **LangChain**, **FastAPI** und optionalem **MQTT**/Speicher aufzubauen. Es läuft auf einem Android-Gerät via **Termux**, ist leichtgewichtig, aber ausbaufähig hin zu einem verteilten System mit autonomen Agenten.

---

## 🚀 Zielsetzung

Ein lokal lauffähiges Backend, das:

* Anfragen an einen KI-Agenten über HTTP erlaubt
* Werkzeuge ("Tools") zur Informationsbeschaffung, Berechnung etc. nutzt
* Mit Gedächtnis arbeitet, um Kontexte zu erkennen
* Später mehrere Agentenrollen und ein Event-basiertes System integrieren kann

---

## 📦 Architekturübersicht

```text
[Client / CURL / App / Browser]
        |
    [FastAPI REST-Backend]
        |
    [LangChain Agent]
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

---

## 🔜 Geplante Erweiterungen

### 🔄 Phase 3b: Sessionverwaltung

* Mehrere Nutzer/Sitzungen unterstützen (UUIDs)
* Speicherbare Dialogverläufe als JSON

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

## ▶️ Start (lokal in Termux)

```bash
uvicorn main:app --host 0.0.0.0 --port 7860
```

---

## 📁 Projektstruktur (aktuell)

```text
project/
├── main.py           # FastAPI-App mit Agentenlogik
├── requirements.txt  # (optional) Paketliste
└── README.md         # Projektdokumentation
```

---

## ✍️ Pflegehinweis

Diese Datei wird mit jeder Entwicklungsphase erweitert, um Struktur, Zielbild und aktuelle Implementierung stets nachvollziehbar zu dokumentieren.

---

Letzter Stand: Phase 3 – Agent mit Memory
