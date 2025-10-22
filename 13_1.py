'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
'''
from flask import Flask, Response
import json
app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    vastaus={}
    if luku <=1:
        vastaus = {
            "Number": luku,
            "isPrime": False
        }
        jsonvastaus = json.dumps(vastaus)
        return Response(jsonvastaus, mimetype='application/json')
    alkuluku=True
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku=False
            vastaus={
                "Number":luku,
                "isPrime":False
            }
    if alkuluku==True:
        vastaus = {
            "Number": luku,
            "isPrime":True
        }
    jsonvastaus = json.dumps(vastaus)
    return Response(jsonvastaus, mimetype='application/json')




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)