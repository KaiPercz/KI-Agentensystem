
## 🔄 Nutzung von direnv mit venv

Dieses Projekt unterstützt [direnv](https://direnv.net/), um die Python-Virtualenv automatisch zu laden:

### Einrichtung

```bash
sudo apt install direnv
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc   # oder ~/.zshrc
source ~/.bashrc                                 # oder ~/.zshrc
```

### Aktivierung im Projekt

```bash
cd <projektverzeichnis>
direnv allow
```

Dann wird bei jedem Verzeichniswechsel automatisch das virtuelle Environment `./venv` geladen.
