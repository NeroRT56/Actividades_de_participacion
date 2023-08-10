#una funcion para calcular la media aritmetica de una lista 
def media_aritmetica(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media

numeros = []
n = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(n):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

resultado = media_aritmetica(numeros)
print("La media aritmética de la lista es:", resultado)