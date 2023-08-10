numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 == 0:
    print("no se puede dividir entre cero ")
else: 
    division = numero1 / numero2
    print("La división de", numero1, "y", numero2, "es", division)

print("La suma de", numero1, "y", numero2, "es", suma)
print("La resta de", numero1, "y", numero2, "es", resta)
print("La multiplicación de", numero1, "y", numero2, "es", multiplicacion)
