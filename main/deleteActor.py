from flask import Flask, render_template, request
import psycopg2 as pg
from dbconfig import DB_CONFIG

app = Flask(__name__)

@app.route('/')
def deleteActorPage():
    return render_template('deleteActor.html')

@app.route('/deleteActor/<int:actor_id>', methods=['DELETE'])
def deleteActor(actor_id):

    conn = pg.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = """
        DELETE FROM actor WHERE actor_id = %s
        """
    cursor.execute(query, (actor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Actor {actor_id} deleted successfully"

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)