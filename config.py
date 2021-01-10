from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8650ff27b20705ec19f9f40a2bc15d76'
app.config['TEMPLATES_AUTO_RELOAD'] = True

"""
app.config['MYSQL_DATABASE_HOST'] = 'softmasterlab.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'softmasterlab'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwerty_1029384756'
app.config['MYSQL_DATABASE_DB'] = 'softmasterlab$hrdep_db'
"""

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'hrdep_db'

mysql = MySQL()
mysql.init_app(app)
