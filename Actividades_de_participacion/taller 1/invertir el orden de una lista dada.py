#invertir el orden de una lista dada 
def invertir_lista(lista):
    lista.reverse()
    return lista
def invertir_lista(lista):
    return lista[::-1]
lista = [2, 2, 11, 45, 54]
lista.reverse()
print(lista)