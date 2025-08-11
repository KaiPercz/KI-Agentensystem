# KI-Agentensystem
Entwicklung unterschiedlicher Ansätze von Agentensystemen für KI-Anwendungen

Dieses Projekt verfolgt das Ziel, ein **modulares Agentensystem** auf Basis von **LangChain**, **Node-Red**, **FastAPI** und optionalem **MQTT**/Speicher aufzubauen.

## **Projektbeschreibung: KI-gestützter E-Mail-Triggerprozess mit Node-RED und Langflow**
📘 Agenten-Backend mit LangChain (Langflow + Node-Red) und FastAPI (Ubuntu-kompatibel) im Verzeichnis "Agenten-Backend_Ubuntu"

### **1. Ausgangslage und Zielsetzung**

Das Projekt zielt darauf ab, eingehende E-Mails automatisiert zu verarbeiten, deren Inhalte zu analysieren und durch geeignete KI-Agenten beantworten zu lassen. Dabei steht die flexible, modulare und erweiterbare Prozessgestaltung im Vordergrund, um sowohl strukturierte als auch unstrukturierte Daten effizient zu verarbeiten.

---

### **2. Derzeitiger Implementierungsstand (Prototyp)**

#### **2.1 Prozessauslöser**

* Der **Trigger** des Prozesses ist eine E-Mail, die an die Adresse `test@ai.percz.de` gesendet wird.
* Absender können Benutzer des Systems sein, die Fragen, Anfragen oder Dokumente zur Verarbeitung einreichen.

#### **2.2 Verarbeitungsschritte im Prototyp**

1. **E-Mail-Analyse**

   * Die eingehende E-Mail wird serverseitig empfangen, analysiert und in ein strukturiertes **JSON-Format** umgewandelt.
   * Im JSON enthalten sind die relevanten Felder wie `from`, `subject`, `body` sowie ggf. Metadaten.

2. **Übergabe an Node-RED**

   * Das JSON-Objekt wird an die Plattform **Node-RED** übermittelt.
   * **Node-RED** übernimmt die **Prozesssteuerung** und entscheidet anhand von Analyseergebnissen, welcher nachgelagerte KI-Agent zuständig ist.

3. **Ansteuerung von Langflow-Agenten**

   * Die ermittelten Daten werden an einen passenden **Langflow-Agenten** übergeben.
   * Langflow übernimmt die KI-gestützte Inhaltsverarbeitung und erstellt eine inhaltliche Antwort.

4. **Ergebnisrückgabe**

   * Das Arbeitsergebnis aus Langflow wird an **Node-RED** zurückgegeben.
   * Node-RED übernimmt die **Formatierung und Aufbereitung** der Antwort.
   * Die fertige Antwort wird **per E-Mail an den ursprünglichen Absender** zurückgesendet.

**Hinweis zum Architekturansatz:**

* Die Gestaltung der Prozesse erfolgt primär in Node-RED, da Langflow in der aktuellen Form nur eingeschränkte Prozesslogik unterstützt.
* Langflow wird ausschließlich für KI-spezifische Verarbeitungen eingesetzt.

---

### **3. Geplante Erweiterungen**

#### **3.1 Verarbeitung von E-Mail-Anhängen**

* **Ziel:**
  Anlagen (z. B. PDF, DOCX, TXT) aus eingehenden E-Mails automatisch auslesen.
* **Weiterverarbeitung:**

  * Textinhalte werden extrahiert und in einer **Vektor-Datenbank** (z. B. ChromaDB) gespeichert.
  * Die Datenbank dient zur späteren semantischen Suche und Anreicherung von Antworten.

#### **3.2 Dynamische Prompt-Steuerung**

* **Aktueller Stand:**
  Prompts (Eingabeaufforderungen für KI) sind aktuell fest in Langflow hinterlegt.
* **Zukunftsidee:**
  Auslagerung der Prompt-Generierung in Node-RED, um diese **zur Laufzeit** flexibel anpassen zu können.
* **Vorteile:**

  * Kontextsensitive Steuerung abhängig vom E-Mail-Inhalt
  * Einfache Anpassung ohne Änderungen am Langflow-Setup
  * Möglichkeit zur A/B-Testung unterschiedlicher Prompt-Varianten

#### **3.3 Erweiterte Agenten-Architektur**

* Mehrere spezialisierte Langflow-Agenten für unterschiedliche Fachgebiete (z. B. technische Anfragen, Kundenservice, Dokumentenprüfung).
* Automatische Klassifizierung der E-Mail-Inhalte zur Auswahl des optimalen Agenten.

#### **3.4 Monitoring und Analyse**

* Aufbau eines Dashboards in Node-RED zur **Live-Überwachung** der Prozesskette.
* Statistische Auswertungen zu E-Mail-Volumen, Antwortzeiten und Themenbereichen.

---

### **4. Mögliche zukünftige Entwicklungspfade**

1. **Integration weiterer KI-Modelle**

   * Neben Langflow könnten Modelle wie **Ollama** oder **OpenAI API** für spezielle Aufgaben eingebunden werden.
2. **Mehrsprachige Verarbeitung**

   * Automatische Spracherkennung und Übersetzung der Inhalte vor Übergabe an den Agenten.
3. **Selbstlernende Routing-Logik**

   * Einsatz von Machine-Learning-Modellen zur Auswahl des passenden Agenten basierend auf historischen Erfolgsquoten.

---

### **5. Zusammenfassung**

Der aktuelle Prototyp zeigt eine funktionierende Ende-zu-Ende-Verarbeitung von E-Mails mit automatisierter KI-Beantwortung.
Node-RED übernimmt dabei die **Prozesssteuerung**, Langflow die **KI-Verarbeitung**.
Zukünftige Erweiterungen zielen auf **höhere Flexibilität**, **umfangreichere Datenverarbeitung** und **bessere Steuerbarkeit** ab.

***

## **Projektbeschreibung: KI-gestützter E-Mail-Triggerprozess mit Node-RED und Langflow**
📘 Agenten-Backend für Android, entwickelt auf der Ubuntu Umgebungen im Verzeichnis "Android"

### **1. Ausgangslage und Zielsetzung**

Das Projekt zielt darauf ab, die Funktionalität auf einem Android basierendem Gerät zu portieren. Das ist mit dem Einsatz von Node-Red gewährleistet, sodass nachfolgend spezifische Installationsbedingungen für diese Plattform dokumentiert werden.

---

### **2. Derzeitiger Implementierungsstand (on hold)**
Mit Ausnahme vom Setup, erfolgt eine Abbildung im vorher stehenden Projekt

***

## **Projektbeschreibung: KI-gestützter E-Mail-Triggerprozess mit Node-RED und langchain.js als Erweiterung für Node-Red**
📘 Agenten-Backend mit Node-Red und spezifischen selbst entwickelten Erweiterungen basierend auf langchain.js im Verzeichnis "Agenten-Backend"

### **1. Ausgangslage und Zielsetzung**

Das Projekt zielt darauf ab, eingehende E-Mails automatisiert zu verarbeiten, deren Inhalte zu analysieren und durch geeignete KI-Agenten beantworten zu lassen. Dabei steht die flexible, modulare und erweiterbare Prozessgestaltung im Vordergrund, um sowohl strukturierte als auch unstrukturierte Daten effizient zu verarbeiten.

---

### **2. Derzeitiger Implementierungsstand (angestrebtes Zielsystem)**
in Planung





