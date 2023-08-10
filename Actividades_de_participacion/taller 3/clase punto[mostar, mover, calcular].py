# clase punto
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mostrar (self):
        print(self.x, self.y)

    def moverse (self, x, y):
        self.x = x
        self.y = y 
    def calcular_distancia (self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

punto1 = Punto(3, 4)
punto1.mostrar()  
punto1.moverse(5, 6)
punto1.mostrar()  
punto2 = Punto (8, 9)
punto2.mostrar()
punto2.moverse(2, 1)
punto2.mostrar()
distancia = punto1.calcular_distancia(punto2)
print("La distancia entre los puntos es:", distancia ) 