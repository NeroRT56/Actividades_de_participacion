# clase circulo [area, perimetro, si un punto pertenece al circulo]
import math
class cirulo:
    def __init__(self, centro, radio,):
        self.centro = centro 
        self.radio = radio 
    def area_circulo(self):
        area = math.pi * self.radio ** 2
        return area 
    def perimetro_circulo(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
# me falta el punto 
