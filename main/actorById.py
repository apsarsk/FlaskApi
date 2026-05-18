from flask import Flask,render_template,request
import psycopg2 as pg 
from dbconfig import  DB_CONFIG

app=Flask(__name__)

@app.route('/getActorById')
def getActorById():
    actor_id = request.args.get('id')
    conn=pg.connect(**DB_CONFIG)
    cursor=conn.cursor()
    query = """
        SELECT * FROM actor
        WHERE actor_id = %s
    """
    cursor.execute(query,(actor_id,))
    row=cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('actorById.html', row=row)