#numero mas grande y mas pequeño en una lista 
numeros = []
n = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(n):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

maximo = max(numeros)
minimo = min(numeros)

print(f"El número más grande es: {maximo}")
print(f"El número más pequeño es: {minimo}")