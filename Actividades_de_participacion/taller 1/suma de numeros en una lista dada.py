#suma de numeros en una lista dada 
numeros = []
n = int(input("Ingrese la cantidad de números que desea sumar: "))
for i in range(n):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma = 0
for num in numeros:
    suma += num

print(f"La suma de los números es: {suma}")