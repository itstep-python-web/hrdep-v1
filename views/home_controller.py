from flask import render_template
from config import app, mysql


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        dep_list = []
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM departments')
        for row in cursor.fetchall():
            dep_list.append({
                'id': row['id'], 'name': row['name']
            })
        return render_template('home/index.html', context={
            'page_title': 'Главная',
            'departments': dep_list
        })
