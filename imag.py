from PIL import Image, ImageDraw
import numpy as np
import random


def distance(x,y):
    a = np.array(x)
    b = np.array(y)
    dist = np.linalg.norm(a-b)
    return dist

def resize(number, imag):
    w,h = r.size
    return imag.resize((number,int(number*h/w)))

def k_mean(n_array, centroid):
    summes = [np.array((0,0,0)) for x in range(len(centroid))]
    cantidades = [0 for x in range(len(centroid))]
    
    for x in range(int(width)):
        for y in range(int(height)):
            indice = 0
            maxi = 100000000000
            for ix, j in enumerate(centroid):
                g = distance(n_array[x][y],j)
                #print("{} distance from {} - {}".format(g,str(n_array[x][y]),str(j)) )
                if g < maxi:
                    maxi = g
                    indice = ix
            summes[indice]+= n_array[x][y]
            cantidades[indice] += 1
    print("{} con sumas {}".format(str(summes),str(cantidades)))
    #input()
    nuevos = [ (summes[i]/cantidades[i]).astype(int) if cantidades[i] != 0 else summes[i] for i in range(len(summes)) ]
    return nuevos

def color_image(dw, n_array, centroid, colors):
    for x in range(int(width)):
        for y in range(int(height)):
            indice = 0
            maxi = 100000000000
            for ix, j in enumerate(centroid):
##                print(str(j) + " " + str(ix))
                g = distance(n_array[x][y],j)
##                print("{} distance from {}".format(g,str(j)) )
                if g < maxi:
                    maxi = g
                    indice = ix
            dw.point( (x,y), fill = colors[indice] )
    
    
file = 'dog.jpg'
r = Image.open(file)
r = resize(512,r)

width, height = r.size
draw = ImageDraw.Draw(r)


K = 3

initial = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for x in range(K)]

## Arreglo bueno
new_array = []
for x in range(int(width)):
   new_array.append([])
   for y in range(int(height)):
       pixel = r.getpixel(( x,y))
       new_array[x].append(np.array(pixel))

print("Generated")

color_image(draw,new_array,initial,tuple(map(tuple, initial)))
r.save('first.png')
for x in range(5):
    print("Starting iteration")
    initial = k_mean(new_array,initial)
    print("Done iteration {}".format(x))
##    print("{} nuevos pesos".format(str(initial)))
    color_image(draw,new_array,initial,tuple(map(tuple, initial)))
    print("Coloreado")
    r.save('{}{}'.format(x,file))
    

