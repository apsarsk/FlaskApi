import psycopg2 as pg
from dbconfig import DB_CONFIG

from flask import Flask,render_template, request
import math

from actorById import getActorById
from postApi import postApi
from deleteActor import deleteActor, deleteActorPage
from updateActor import updateActor,updateActorPage 



app=Flask(__name__)
@app.route('/getApi')
def getApi():
    page=int(request.args.get('page',1))
    limit=int(request.args.get('limit',25))
    offset=(page-1)*limit
    conn=pg.connect(**DB_CONFIG)
    cursor=conn.cursor()
    query = """
        SELECT * FROM actor
        ORDER BY actor_id
        LIMIT %s OFFSET %s
    """
    cursor.execute(query,(limit,offset))
    rows=cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM actor")
    total_records=cursor.fetchone()[0]
    

    total_pages = math.ceil(total_records / limit)


    cursor.close()
    conn.close()
    return render_template('getApi.html', rows=rows, page=page, total_pages=total_pages)
@app.route('/')
def home():
    return render_template('searchActor.html')

@app.route('/saveActor')
def saveActor():
    return render_template('postApi.html')

app.add_url_rule(
    '/getActorById',
    view_func=getActorById
)

app.add_url_rule(
    '/postApi',
    view_func=postApi,methods=['GET','POST']
)

app.add_url_rule(
    '/deleteActor/<int:actor_id>',
    view_func=deleteActor,methods=['DELETE']
)

app.add_url_rule(
    '/deleteActor',
    view_func=deleteActorPage,methods=['GET']
)

app.add_url_rule(
    '/updateActor',
    view_func=updateActorPage,methods=['GET']
)

app.add_url_rule(
    '/updateActor/<int:actor_id>',
    view_func=updateActor,methods=['PUT']
)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




