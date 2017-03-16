import matplotlib.pyplot as plt
import numpy as np
import random
import pandas

'''
    Calcula la distancia euclideana entre 2 vectores
    x: primer vector
    y: segundo vector
'''
def distance(x,y):
    a = np.array(x)
    b = np.array(y)
    dist = np.linalg.norm(a-b)
    return dist

def k_mean(n_array, centroid):
    n_centros = len(centroid)
    summes = [np.array((0.0,0.0,0.0,0.0)) for x in range(n_centros)]
    cantidades = [0 for x in range(n_centros)]
    for x in range(len(n_array)):
            indice = 0
            maxi = 100000000000
            for ix, j in enumerate(centroid):
                g = distance(n_array[x],j)
                if g < maxi:
                    maxi = g
                    indice = ix
            summes[indice]+= n_array[indice]
            cantidades[indice] += 1
    cantidades = list(map(float,cantidades))
    nuevos = [ (summes[i]/cantidades[i]) if cantidades[i] != 0 else summes[i] for i in range(len(summes)) ]
    return nuevos

def getIndice(s):
    if(s == "Iris-setosa"):
        return 0
    elif(s == "Iris-versicolor"):
        return 1
    else:
        return 2

def iniciar(d, k):
    l = data.shape[0]-1
    initial = [random.randint(0,l) for j in range(k)]
    centros = d.iloc[initial]
    return centros

k = 5
clusters = [[] for i in range(k)]
conteo = [[0,0,0] for i in range(k)]
clasificacion = []

data = pandas.read_table("bezdekIris.data",sep=",", header=None)
print(data[4][148])
centros = iniciar(data,k)
datos = data.iloc[:,:4].as_matrix()
initial = centros.iloc[:, :4].as_matrix()

for x in range(40):
    initial = k_mean(data.iloc[:, :4].as_matrix(),initial)

for j in range(len(datos)):
    indice = 0
    distancia = 100000000000
    for i in range(len(initial)):
        g = distance(datos[j],initial[i])
        if(g < distancia):
            distancia = g
            indice = i
    clusters[indice].append(j)
    conteo[indice][getIndice(data[4][j])] += 1
print(conteo)

for i in range(len(conteo)):
    maxi = 0
    indice = 0
    for j in range(len(conteo[i])):
        if(conteo[i][j] > maxi):
            maxi = conteo[i][j]
            indice = j
    if(indice == 0):
        clasificacion.append("Iris-setosa")
    elif(indice == 1):
        clasificacion.append("Iris-versicolor")
    else:
        clasificacion.append("Iris-virginica")

buenos = 0
malos = 0

for i in range(len(clusters)):
    for j in range(len(clusters[i])):
        if(data[4][clusters[i][j]] == clasificacion[i]):
            buenos += 1
        else:
            malos += 1

print(clasificacion)
print(buenos,malos)