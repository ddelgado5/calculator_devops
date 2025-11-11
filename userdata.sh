#!/bin/bash

# Actualizar paquetes e instalar herramientas necesarias
apt update -y
apt install -y python3-pip python3-venv

# Crear carpeta del proyecto
mkdir -p /home/ubuntu/calculadora
cd /home/ubuntu/calculadora

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar Flask y Gunicorn
pip install flask gunicorn

# Crear un archivo app.py temporal para que el servicio no falle al iniciar
cat <<EOF > app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Calculadora en construcción"
EOF

# Crear archivo de servicio systemd
cat <<EOF > /etc/systemd/system/calculadora.service
[Unit]
Description=Calculadora Flask App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/calculadora
ExecStart=/home/ubuntu/calculadora/venv/bin/gunicorn --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Permisos y arranque del servicio
chown -R ubuntu:ubuntu /home/ubuntu/calculadora
systemctl daemon-reexec
systemctl enable calculadora
systemctl start calculadora
