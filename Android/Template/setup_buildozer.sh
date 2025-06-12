#!/bin/bash

# Exit on error
set -e

echo "🔧 [1/6] Installiere Build-Abhängigkeiten..."
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev \
    xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

echo "☕ [2/6] Installiere OpenJDK 11 (statt default JDK 21)..."
sudo apt install -y openjdk-11-jdk

echo "🧭 [3/6] Setze JAVA_HOME auf OpenJDK 11..."
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"

# In .bashrc dauerhaft ergänzen
if ! grep -q 'JAVA_HOME.*openjdk-11' ~/.bashrc; then
    echo 'export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"' >> ~/.bashrc
    echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc
fi

echo "⬇️ [4/6] Installiere pyenv..."
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if [ ! -d "$PYENV_ROOT" ]; then
    curl https://pyenv.run | bash
fi

# Shell konfigurieren
if ! grep -q 'pyenv init' ~/.bashrc; then
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
fi

# Shell neu laden für aktuelle Session
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

echo "🐍 [5/6] Installiere Python 3.10.13 via pyenv..."
pyenv install -s 3.10.13
pyenv global 3.10.13

echo "📦 [6/6] Erzeuge virtuelle Umgebung, installiere Buildozer + Kivy..."
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install buildozer "kivy[base]" kivymd cython

echo "✅ Setup abgeschlossen!"
echo "ℹ️ Aktiviere die Umgebung mit:"
echo "    source venv/bin/activate"
echo "📦 Starte den Android-Build mit:"
echo "    buildozer android debug"
