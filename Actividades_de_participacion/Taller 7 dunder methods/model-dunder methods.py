#actividad #7 dunder methods
from typing import List
from dataclasses import dataclass

@dataclass

class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.elementos: List[Elemento] = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    # aqui se cololca el atributo privado desde @property
    @property
    def id(self):
        return self.__id

    def contiene_elemento(self, elemento: Elemento) -> bool:
        return elemento in self.elementos


    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene_elemento(elemento):
            self.elementos.append(elemento)


    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)


    def intersectar(self, cls, conjunto1, conjunto2):
        elementos_comunes = [elemento for elemento in conjunto1.elementos if elemento in conjunto2.elementos]
        nombre_conjunto = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        conjunto_interseccion = cls(nombre_conjunto)
        for elemento in elementos_comunes:
            conjunto_interseccion.agregar_elemento(elemento)
        return conjunto_interseccion


    def __str__(self):
        return f"Conjunto {self.nombre}: ({self.elementos_str})"

