from PIL import Image, ImageDraw
import numpy as np
import random

'''
    Calcula la distancia euclideana entre 2 colores
    x: primer color
    y: segundo color
'''
def distance(x,y):
    a = np.array(x)
    b = np.array(y)
    dist = np.linalg.norm(a-b)
    return dist

'''
    Modifica el ancho de una imagen a number, manteniendo la proporcion
    number: nuevo ancho
    imag: Image 
'''
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

                if g < maxi:
                    maxi = g
                    indice = ix
            summes[indice]+= n_array[x][y]
            cantidades[indice] += 1
    print("{} con sumas {}".format(str(summes),str(cantidades)))
    nuevos = [ (summes[i]/cantidades[i]).astype(int) if cantidades[i] != 0 else summes[i] for i in range(len(summes)) ]
    return nuevos

def color_image(dw, n_array, centroid, colors):
    for x in range(int(width)):
        for y in range(int(height)):
            indice = 0
            maxi = 100000000000
            for ix, j in enumerate(centroid):
                g = distance(n_array[x][y],j)
                if g < maxi:
                    maxi = g
                    indice = ix
            dw.point( (x,y), fill = colors[indice] )
  
file = 'perro-nadando.jpg'
r = Image.open(file)
##r = resize(512,r)

width, height = r.size
draw = ImageDraw.Draw(r)

k = 128
initial = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for x in range(k)]
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
print("Coloreando {}".format(k))
color_image(draw,new_array,initial,tuple(map(tuple, initial)))

r.save('{}-{}'.format(k,file))

    

