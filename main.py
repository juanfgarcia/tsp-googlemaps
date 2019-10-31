'''
Solves TSP problem with real location imput.
Copyright (C) 2019  Juan Francisco García Casado, Guillermo Bautista-Abad Acebes
'''

import googlemaps as gm

def setup():
    fp = open('key')
    content = fp.readlines()
    key = content[0]
    client = gm.Client(key)
    return client

def main():
    client = setup()

    origins = ["Perth, Australia", 
                "Sydney, Australia",
                "Melbourne, Australia", 
                "Adelaide, Australia",
                "Brisbane, Australia", 
                "Darwin, Australia",
                "Hobart, Australia", 
                "Canberra, Australia"]

    destinations = ["Uluru, Australia",
                    "Kakadu, Australia",
                    "Blue Mountains, Australia",
                    "Bungle Bungles, Australia",
                    "The Pinnacles, Australia"]

    apiMatrix = client.distance_matrix(origins, destinations)

    matrix = []
    for row in apiMatrix['rows']:
        column = []
        for element in row['elements']:
           column.append(element['duration']['value'])
        matrix.append(column)

    for line in matrix:
        print(line)
            
       

    

  
  

if __name__ == "__main__":
    main()

