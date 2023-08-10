#Funcion fahrenheit a celsius 
def fahrenheit_a_celsius(f):
    c = (f - 32) * 5/9
    return c
temperatura_f = float(input("Ingrese la temperatura en fahrenheit: "))
temperatura_c = fahrenheit_a_celsius(temperatura_f)
print(f"{temperatura_f} grados Fahrenheit son {temperatura_c} grados Celsius")