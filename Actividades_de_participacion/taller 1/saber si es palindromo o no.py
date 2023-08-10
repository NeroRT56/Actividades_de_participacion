#saber si es palindromo o no 
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    for i in range(len(cadena)):
        if cadena[i] != cadena[-i-1]:
            return False
    return True
cadena = input("Ingrese una cadena de texto: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")