import numpy as np
from random import randint as ri
import pygal

class Dado():
    def __init__(self, caras, numero, plus):
        self.caras = caras 
        self.numero = numero
        self.plus = plus
    
    def rodar(self):
        Res = []
        for tirada in range(self.numero):
            Res.append(ri(0, self.caras) + self.plus)
        return Res

def Roll(cadena):
    cadena = cadena.split('d')
    nombre, caras = int(cadena[0]), int(cadena[1])
    Dice = Dado(caras, numero, 0)
    Dice.rodar()

caras = 10
nomine = 10
Multiple_data = [0 for i in range(nomine)]
for i in range(0, 500):
    D = Dado(caras, nomine, 0)
    Data = D.rodar()
    Multiple_data += Data

cont_frec = np.zeros(caras+1)
for dato in Multiple_data:
    for numero in range(caras+1):
        if numero == dato:
            cont_frec[numero] += 1


hist = pygal.Bar()
hist._title = "Frecuancias de las tiradas"
hist.add("frecuencias de resultados del dado", cont_frec)
hist.x_labels = [str(i) for i in range(0, caras+1)]
hist._x_title = "Caras del dado"
hist._y_title = "Frecuancias"
hist.render_to_file(filename="Data Analysis.svg")
