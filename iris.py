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
##    print("Distancia entre {} - {}".format(str(x),str(y)))
    a = np.array(x)
    b = np.array(y)
    dist = np.linalg.norm(a-b)
    return dist

def k_mean(n_array, centroid):
    print(centroid)
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
##            print("Ganador {} con distancia {}".format(j,g))
            summes[indice]+= n_array[indice]
            cantidades[indice] += 1
    print("{} con sumas {}".format(str(summes),str(cantidades)))
    cantidades = list(map(float,cantidades))
    nuevos = [ (summes[i]/cantidades[i]) if cantidades[i] != 0 else summes[i] for i in range(len(summes)) ]
    print("Centros nuevos")
    print(nuevos)
    print()
    return nuevos


def iniciar(d, k):
    l = data.shape[0]-1
    initial = [random.randint(0,l) for j in range(k)]
    centros = d.iloc[initial]
    return centros

k = 3
data = pandas.read_table("bezdekIris.data",sep=",", header=None)
centros = iniciar(data,k)
initial = centros.iloc[:, :4].as_matrix()
print("Centros iniciales")
print(initial)
print()
for x in range(40):
    print("Starting iteration")
    initial = k_mean(data.iloc[:, :4].as_matrix(),initial)
    print("Done iteration {}".format(x))
