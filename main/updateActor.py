from flask import Flask, jsonify,render_template, request
import psycopg2 as pg
from dbconfig import DB_CONFIG
app =Flask(__name__)

@app.route('/updateActor',methods=['GET'])
def updateActorPage():
    return render_template('updateActor.html')

@app.route('/updateActor/<int:actor_id>', methods=['POST'])
def updateActor(actor_id):

    data=request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')

    conn = pg.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query ="""

        UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s"""
    
    cursor.execute(query,(first_name,last_name,actor_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "message": f"Actor {actor_id} updated successfully"
    })