import itertools
import sys

# Funcion auxiliar para restar un elemento de un conjunto
def resta(tupla, elem):
    result=[]
    for i in tupla:
        if i!=elem:
            result.append(i)
    return tuple(result)

# Implementacino del algoritmo de Hel-Karp, recibe una matriz de distancias
# y devuelve el coste como entero y el camino como un array
def Held_Karp(matriz):
    N=len(matriz)
    V=[]
    
    path=[]
    path.append(0)

    for i in range(1, N):
        V.append(i)

    V=tuple(V)

    # Guardamos en un diccionario los costes de los subproblemas optimos 
    # dic[S, i] representa el coste de recorrer el subconjunto S pasando una vez
    # por cada nodo, empezando en 1 y acabando en i.
    dic = {}

    #Inicializamos los caminos de un solo elemento
    for i in range(1, N):
        dic[(i,), i]=matriz[0][i]

    #Para cada subconjunto posible (2^n posibles) calculamos el coste minimo 
    for size in range(2,N):
        for subset in itertools.combinations(range(1,N), size):
            for k in subset:
                aux = resta(subset,k)
                lista=[]
                for m in subset:
                    if (m!=k):
                        lista.append(dic[aux, m]+ matriz[m][k])
                dic[subset, k] = min(lista)


    # Calculamos el minimo de todos los caminos que recorren todos los vertices
    subset=V
    lista = []
    for i in range(1,N):
        lista.append(dic[subset, i] + matriz[i][0])

    #Obtemenos el ultimo vertice antes de ir a 0
    coste = min(lista)
    last = lista.index(coste)+1
    path.append(last)

    # Hacemos backtracking para recuperar el camino final
    subset = resta(subset, last)
    for i in range(1, N-1):
        subset = resta(subset, last)
        lista = []
        pos = []
        for j in subset:
            lista.append(dic[subset, j])
            pos.append(j)
        Min = min(lista)
        last = pos[lista.index(Min)]
        path.append(last)

    path.append(0)
    return path, coste

