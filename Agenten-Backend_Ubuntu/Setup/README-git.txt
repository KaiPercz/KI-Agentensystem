Gitea installieren (Leichtgewichtige Weboberfläche)
##########################################
sudo apt update
sudo apt upgrade
sudo apt install git sqlite3
##########################################

sudo adduser --system --group --disabled-password --shell /bin/bash --home /home/git --gecos 'Gitea' git

Website zum prüfen der aktuellen Version: https://dl.gitea.com/gitea/

wget -O /tmp/gitea https://dl.gitea.io/gitea/1.24.2/gitea-1.24.2-linux-amd64
sudo mv /tmp/gitea /usr/local/bin/gitea
sudo chmod +x /usr/local/bin/gitea

sudo mkdir -p /var/lib/gitea/{custom,data,log}
sudo chown -R git:git /var/lib/gitea/
sudo chmod -R 750 /var/lib/gitea/
sudo mkdir /etc/gitea
sudo chown root:git /etc/gitea
sudo chmod 770 /etc/gitea

sudo vi /etc/systemd/system/gitea.service

-----------------------
[Unit]
Description=Gitea (Git with a cup of tea)
After=syslog.target
After=network.target

[Service]
RestartSec=2s
Type=simple
User=git
Group=git
WorkingDirectory=/var/lib/gitea/
ExecStart=/usr/local/bin/gitea web --config /etc/gitea/app.ini
Restart=always
Environment=USER=git HOME=/home/git GITEA_WORK_DIR=/var/lib/gitea

[Install]
WantedBy=multi-user.target
-----------------------

sudo systemctl daemon-reload
sudo systemctl start gitea
sudo systemctl enable gitea

Navigieren Sie in Ihrem Webbrowser zu http://127.0.0.1:3000. Sie werden von der Gitea-Installationsseite begrüßt.
###################################################
