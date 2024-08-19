# Configurare Django pe un server Ubuntu

Pasii necesari pentru server

## 1. Actualizare server

Actualizare pachete

```bash
sudo apt update
sudo apt upgrade
```
## 2. Instalare dependințe

Instalați toate pachetele necesare pentru a rula aplicația Django.

### Python și pip
```bash
sudo apt install python3-pip python3-dev libpq-dev
```
### Git (dacă e nevoie să clonezi proiectul dintr-un repository)
```bash
sudo apt install git
```
### Server web Nginx
```bash
sudo apt install nginx
```
### Server WSGI Gunicorn
```bash
sudo pip3 install gunicorn
```
## 3. Configurarea aplicației Django

### Clonează proiectul Django (dacă este necesar)
```bash
git clone https://exemplu.com/proiect.git
cd proiect
```
### Creează și activează un mediu virtual
```bash
python3 -m venv venv
source venv/bin/activate
```
### Instalează pachetele necesare
```bash
pip install -r requirements.txt
```
### Realizează migrațiile bazei de date
```bash
python manage.py migrate
```
### Colectează fișierele statice
```bash
python manage.py collectstatic
```
### Testează local cu Gunicorn
```bash
gunicorn --bind 0.0.0.0:8000 proiect.wsgi:application
```
## 4. Configurarea serverului web Nginx

### Configurează Nginx pentru a servi aplicația
Creează un fișier de configurare Nginx pentru aplicația Django.
```bash
sudo nano /etc/nginx/sites-available/proiect
```
Adauga urmatorul continut:
```bash
server {
    listen 80;
    server_name example.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/project/proiect.sock;
    }
}
```
### Activeaza configurarea Nginx
```bash
sudo ln -s /etc/nginx/sites-available/proiect /etc/nginx/sites-enabled
```
### Verifică configurația Nginx pentru erori
```bash
sudo nginx -t
```
### Repornește Nginx
```bash
sudo systemctl restart nginx
```

## 5. Configurarea serviciului Gunicorn

### Creează un fișier de serviciu systemd pentru Gunicorn
```bash
sudo nano /etc/systemd/system/gunicorn.service
```
Adaugă următorul conținut:

```bash
[Unit]
Description=gunicorn daemon for Django project
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/project/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/project/proiect.sock proiect.wsgi:application

[Install]
WantedBy=multi-user.target
```
### Porneste serviciul Gunicorn
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### Verifică dacă Gunicorn rulează corect
```bash
sudo systemctl status gunicorn
```

## 6. Configurează DNS-ul pentru domeniu astfel încât să pointeze către IP-ul serverului.

## 7. Configurarea SSL

### Instalează Certbot
```bash
sudo apt install certbot python3-certbot-nginx
```
### Instalează un certificat SSL
```bash
sudo certbot --nginx -d example.com -d www.example.com
```
### Verifica certificatul SSL
```bash
sudo certbot renew --dry-run
```
## 8. Depanare și securitate
### Verifică jurnalele
Verifică jurnalele Nginx și Gunicorn pentru a depana orice probleme.
```bash
sudo journalctl -u gunicorn
sudo tail -f /var/log/nginx/error.log
```

### Setează permisiunile fișierelor și directoarelor

### Asigură-te că permisiunile fișierelor și directoarelor sunt setate corect pentru a preveni accesul neautorizat.
