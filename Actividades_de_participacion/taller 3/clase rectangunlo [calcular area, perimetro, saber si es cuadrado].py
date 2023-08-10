# clase rectangunlo [calcular area, perimetro, si es cuadrado]
class Rectangulo:
    def __init__(self, l1, b1):
        self.l1 = l1
        self.b1 = b1 
    def perimetro (self):
            per = 2*self.l1 + 2* self.b1 
            return per
    def area_rectangulo (self):
         area = self.b1 * self.l1
         return area 
    def saber_cuadrado (self):
        if self.l1 == self.b1 :
            print("Es un cuadrado")
        else:
            print("no es un cuadrado")
    
rectangulo1 = Rectangulo(4, 5)
perimetro = rectangulo1.perimetro()
area_del_rectangulo = rectangulo1.area_rectangulo()
cuadrado = rectangulo1.saber_cuadrado()
print("El perimetro es: ", perimetro)
print("El Area del rectangulo es: ", area_del_rectangulo)
