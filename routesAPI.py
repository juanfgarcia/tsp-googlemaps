from flask import Flask, Response, render_template
import googlemaps as gm
import json
from tsp import Held_Karp

app = Flask(__name__, template_folder='templates')

def setup():
    fp = open('key')
    content = fp.readlines()
    key = content[0]
    client = gm.Client(key)
    return client

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cities/<string:cities>", methods=['GET'])
def getTour(cities):
    citieslist = []
    for string in cities.split("_"):
        citieslist.append(string.replace('-',', '))

    matrix = getMatrix(citieslist)
    path, cost = Held_Karp(matrix)
    pathlist = []
    for node in path:
        pathlist.append(citieslist[node])

    return Response(json.dumps(pathlist), mimetype='application/json')

    
def getMatrix(citieslist):
    client = setup()

    apiMatrix = client.distance_matrix(citieslist, citieslist)

    matrix = []
    for row in apiMatrix['rows']:
        column = []
        for element in row['elements']:
           column.append(element['duration']['value'])
        matrix.append(column)
    
    return matrix





if __name__=='__main__':
    app.run(debug=True)