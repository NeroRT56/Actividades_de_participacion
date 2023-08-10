import math

def calcular_area_circulo(radio):
    
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    area = math.pi * (radio ** 2)
    return area
radio = float(input("Ingrese el radio: "))
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)