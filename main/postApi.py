from flask import Flask, render_template, request

import psycopg2 as pg
from dbconfig import DB_CONFIG

app = Flask(__name__)
@app.route('/postApi', methods=['GET','POST'])
def postApi():
    message = ""
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        conn=pg.connect(**DB_CONFIG)
        cursor=conn.cursor()
        query="""
            Insert into actor (first_name,last_name) values(%s,%s)"""
        rows=cursor.execute(query,(first_name,last_name))
        conn.commit()
        cursor.close()
        conn.close()
        message = "Actor inserted successfully"
    return render_template('postApi.html', message=message)