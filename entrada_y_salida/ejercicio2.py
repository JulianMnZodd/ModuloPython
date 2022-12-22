from pickle import *

class Auto:

    def __init__(self, color, puertas,ruedas):
        self.color = color
        self.puertas = puertas
        self.ruedas=ruedas

    def __str__(self):
        return self.color + " " + self.puertas+ " " + self.ruedas


fitito = Auto("Azul", "4","4")
print(fitito)

file = open('Auto_objeto', 'w+b')

dump(fitito, file)

file.seek(0)
nuevo_fitito = load(file)

print(nuevo_fitito)
file.close()