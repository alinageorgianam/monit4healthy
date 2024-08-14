import os
import django
import MySQLdb
from django.contrib.auth.hashers import make_password

# Configurarea Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monit4healthy.settings')
django.setup()

# Conectează-te la baza de date MySQL
db = MySQLdb.connect("localhost", "root", "3516208127127", "acu")
cursor = db.cursor()

# Selectează utilizatorii
cursor.execute("SELECT id_doc, password FROM doctori")
users = cursor.fetchall()

# Actualizează parolele criptate
for user in users:
    user_id = user[0]
    plain_password = user[1]
    hashed_password = make_password(plain_password)  # Criptează parola
    cursor.execute("UPDATE doctori SET password = %s WHERE id_doc = %s", (hashed_password, user_id))

# Salvează modificările
db.commit()
cursor.close()
db.close()
