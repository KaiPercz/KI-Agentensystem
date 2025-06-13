# 📱 Python-Apps als APK auf Android mit Kivy & Buildozer

Dieses Projekt zeigt, wie man **Python-Anwendungen direkt auf Android** ausführt, indem man daraus **echte APK-Dateien** erstellt. Ziel ist es, auf einfache Weise interaktive grafische Benutzeroberflächen (GUIs) mit **Kivy** oder **KivyMD** zu entwickeln und auf Android-Geräten lauffähig zu machen – ganz ohne Java oder Kotlin.

---

## 🎯 Zielsetzung

- Entwicklung und Test von **grafischen Python-Apps** für Android
- Nutzung von **Kivy** für GUI-Erstellung
- Einsatz von **Buildozer** zum Kompilieren von **APK-Dateien**
- Entwicklungsumgebung: **Ubuntu 24.x**
- Kein Root, kein Android Studio notwendig

---

## 🧰 Genutzte Komponenten

| Komponente | Zweck |
|------------|-------|
| **Python 3.10**  | Programmiersprache |
| **OpenJDK 11**   | Programmiersprache |
| **Kivy**         | GUI-Framework für plattformübergreifende Apps |
| **KivyMD**       | Material Design-Erweiterung für Kivy |
| **Buildozer**    | Toolchain zur Erstellung von APK-Dateien aus Python-Code |
| **Ubuntu 24.x**  | Entwicklungsplattform |

---

## 📦 Beispiel: Hello World App

Ein einfaches Beispiel befindet sich in `main.py`.



⚙️ Entwicklungsumgebung vorbereiten (Ubuntu 24.x)

# Systempakete installieren
im Repository befindet sich die Setup Routine: KI-Agentensystem/Android/Template/setup_buildozer_ubuntu24.sh

ggf. müssen die Rechte vor der Ausführung angepasst werden
```bash
sudo apt install openjdk-11-jdk
sudo apt remove --purge gradle
rm -rf ~/.buildozer/android/platform/gradle*
cd /opt
sudo wget https://services.gradle.org/distributions/gradle-7.4.2-bin.zip
sudo unzip gradle-7.4.2-bin.zip
sudo ln -sfn /opt/gradle-7.4.2 /opt/gradle
echo 'export PATH="/opt/gradle/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

chmod +x setup_buildozer.sh
cd ..
./Template/setup_buildozer.sh
```

Repository klonen (bzw. Projektstruktur kopieren)
```bash
git clone https://github.com/KaiPercz/KI-Agentensystem.git
cd KI-Agentensystem
cd Android
```

## 💡 Herleitung der virtuelle Umgebung mit direnv
### ✅ Vorteile durch venv + direnv

| Vorteil | Beschreibung |
|--------|--------------|
| Isoliert | Kein Risiko von Versionskonflikten mit globalem Python |
| Wiederholbar | Projektabhängigkeiten klar definiert |
| Automatisch | Aktivierung erfolgt automatisch beim Projektwechsel |
| Kompatibel | Funktioniert gut mit Git und CI/CD-Systemen |

Zur Isolierung der Python-Umgebung kann `direnv` verwendet werden:

```bash
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc 
exec $SHELL
```

Umgebung initialisieren
```bash
python3 -m venv venv
source ./venv/bin/activate
```

zum Verlassen der Umgebung: "deactivate" eingeben

```bash
echo 'layout python3' > .envrc
direnv allow
```

# Buildozer und Kivy installieren
```bash
pip install --upgrade pip

pip install -r requirements.txt
 oder
pip install buildozer "kivy[base]" kivymd
```

🔧 Projekt initialisieren
```bash
buildozer init
```

📁 Projektstruktur (Beispiel)
```text
my-kivy-app/
├── .direnv/                # Automatisch erzeugt durch direnv (virtuelle Umgebung)
├── .envrc                  # direnv-Konfiguration für die venv-Aktivierung
├── .gitignore              # Ignoriert .direnv, __pycache__, buildozer-builds etc.
├── buildozer.spec          # Konfiguration für Buildozer
├── main.py                 # Einstiegspunkt der Kivy-App
├── mylayout.kv             # (optional) Kivy-Layoutdatei
├── requirements.txt        # Abhängigkeiten für pip (z. B. kivy, kivymd, buildozer)
└── README.md               # Dokumentation
```

💡 Vorteile dieser Struktur
```text
| Vorteil                                                    | Nutzen                                        |
| ---------------------------------------------------------- | --------------------------------------------- |
| `.direnv/` hält Umgebung lokal isoliert                    | Kein Einfluss auf globales Python             |
| `.envrc` sorgt für Automatisierung                         | Aktivierung bei Verzeichniswechsel            |
| `.gitignore` schützt vor ungewolltem Committen             | Kein Build-Müll oder lokale Umgebungen in Git |
| `requirements.txt` hält die Abhängigkeiten nachvollziehbar | Gut für Teams oder CI/CD                      |
| `Makefile` erleichtert repetitive Tasks                    | „make build“ statt lange Kommandos merken     |
```


🛠 APK erstellen

```text
| Zweck                          | Befehl                         |
| ------------------------------ | ------------------------------ |
| App bauen                      | `buildozer android debug`      |
| App auf Gerät installieren     | `buildozer android deploy run` |
| Verzeichnisstruktur bereinigen | `buildozer android clean`      |
| Nur APK generieren             | `buildozer android debug`      |
| Neue `buildozer.spec` erzeugen | `buildozer init`               |
```

unbedingt beachten: das Erstellen des Programms benötigt mindestens 5 GByte !

```bash
buildozer -v android debug
```

Nach Abschluss liegt die APK im Verzeichnis:
bin/myapp-0.1-debug.apk

📲 Installation auf Android
APK manuell kopieren oder via ADB installieren:

```bash
adb install bin/myapp-0.1-debug.apk
```
