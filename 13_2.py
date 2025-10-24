'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa:
{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
'''
from flask import Flask, Response
import json
import mysql.connector

yhteys =mysql.connector.connect(
    host="127.0.0.1",
    user="vilho1",
    password="Saunakilpikonna",
    port=3306,
    database="flightgame",
    autocommit=True
)

app = Flask(__name__)
@app.route('/kenttä/<ident>')
def kenttä(ident):
    sql=f'select ident,name, municipality from airport where ident = "{ident}"'
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    vastaus ={
        "icao":tulos[0][0],
        "Name":tulos[0][1],
        "Municipality":tulos[0][2]
    }
    jsonvastaus = json.dumps(vastaus)
    return Response(jsonvastaus, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
