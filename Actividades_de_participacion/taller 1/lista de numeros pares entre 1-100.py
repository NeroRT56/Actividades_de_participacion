#lista de numeros pares entre 1-100
numeros_pares = []
i = 2
while i <= 101:
    if i % 2 == 0:
        print(i)
        i += 2
print(numeros_pares)