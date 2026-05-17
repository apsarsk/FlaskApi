import psycopg2 as pg
from dbconfig import DB_CONFIG

from flask import Flask,render_template, request
import math

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




