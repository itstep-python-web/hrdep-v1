from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8650ff27b20705ec19f9f40a2bc15d76'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_HOST'] = 'softmasterlab.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'softmasterlab'
app.config['MYSQL_PASSWORD'] = 'Qwerty_1029384756'
app.config['MYSQL_DB'] = 'softmasterlab$hrdep_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
