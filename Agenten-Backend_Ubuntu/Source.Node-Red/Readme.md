Diese Anleitung ist ein exemplarischer Leitfaden, um Node-RED lokal in Ubuntu 24.x zu installieren – ohne Docker, mit nvm, um gezielt die richtige Node.js-Version verwenden zu können (empfohlen: Node.js 18.x LTS).

✅ Voraussetzungen

```bash
sudo apt update
sudo apt install -y curl git build-essential
```


1. nvm installieren (Node Version Manager)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Dann nvm in die Shell laden:

```bash
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"
```

sinnvollerweise ergänzt man das in der .bashrc:

```bash
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> ~/.bashrc
```


2. Empfohlene Node.js Version installieren (Node-RED kompatibel)
Node-RED ist stabil mit Node.js 18.x:

```bash
nvm install 18
nvm use 18
nvm alias default 18
```

3. Node-RED global (in Nutzerkontext) installieren

```bash
npm install -g --unsafe-perm node-red
```

4. Node-RED starten
```bash
node-red
```

5. Node-RED beim Boot automatisch starten

```bash
touch ~/.config/systemd/user/node-red.service
```

```bash
[Unit]
Description=Node-RED
After=network.target

[Service]
ExecStart=/home/<dein-benutzername>/.nvm/versions/node/v18.x.x/bin/node-red
Restart=on-failure
Environment=PATH=/home/<dein-benutzername>/.nvm/versions/node/v18.x.x/bin:/usr/bin:/bin
WorkingDirectory=/home/<dein-benutzername>/

[Install]
WantedBy=default.target
```

und aktivieren mittels:

```bash
systemctl --user daemon-reexec
systemctl --user enable node-red
systemctl --user start node-red
```

🔎 Nützliche Befehle
Logs anzeigen:
```bash
journalctl --user -u node-red -f
```

Node-RED stoppen/starten:
```bash
systemctl --user stop node-red
systemctl --user start node-red
```
