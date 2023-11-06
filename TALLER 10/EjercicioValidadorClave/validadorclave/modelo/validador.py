from errores import (Regla1Excepcion, Regla2Excepcion,
                      Regla3Excepcion, Regla4Excepcion)
# TODO: Implementa el código del ejercicio aquí
class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def validar(self, clave):
        if not self._validar_longitud(clave):
            raise ValueError("La clave no cumple con la longitud mínima requerida")

    def _contiene_mayuscula(self, clave):
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave):
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(self, clave):
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

    def validar(self, clave):
        if (not self._contiene_mayuscula(clave) or
            not self._contiene_minuscula(clave) or
            not self._contiene_numero(clave)):
            raise ValueError("La clave no cumple con las reglas de validación")
class ReglaValidacionGanimedes:
    def __init__(self):
        self.caracteres_especiales = "@_#$%"

    def contiene_caracter_especial(self, clave):
        for caracter in clave:
            if caracter in self.caracteres_especiales:
                return True
        return False
    def es_valida(self, clave):
        if self.esta_repetida(clave) or self.no_cumple_con_la_cantidad_minima_de_caracteres(clave) or self.no_tiene_n_caracteres_distintos(clave, n=3):
            return False
        return True
    

class ReglaValidacionCalisto:
    def __init__(self):
        self.palabra_buscada = "calisto"

    def contiene_calisto(self, clave):
        # Buscamos la primera aparición de la palabra en mayúsculas
        primera_aparicion = clave.upper().find(self.palabra_buscada.upper())

        # Si no se encuentra la palabra en mayúsculas, retornamos False
        if primera_aparicion == -1:
            return False

        # Obtenemos el número de letras mayúsculas que hay en la clave antes de la primera aparición de la palabra
        letras_mayusculas_antes = len(clave[:primera_aparicion].upper()) - len(clave[:primera_aparicion].lower())

        # Si hay al menos dos letras mayúsculas antes de la primera aparición de la palabra, retornamos True
        if letras_mayusculas_antes >= 2:
            return True

        # Buscamos la última aparición de la palabra en mayúsculas
        ultima_aparicion = clave.upper().rfind(self.palabra_buscada.upper())

        # Si la última aparición de la palabra es igual a la primera, retornamos False
        if primera_aparicion == ultima_aparicion:
            return False

        # Obtenemos el número de letras mayúsculas que hay en la clave después de la última aparición de la palabra
        letras_mayusculas_despues = len(clave[ultima_aparicion + len(self.palabra_buscada):].upper()) - len(clave[ultima_aparicion + len(self.palabra_buscada):].lower())

        # Si hay al menos dos letras mayúsculas después de la última aparición de la palabra, retornamos True
        if letras_mayusculas_despues >= 2:
            return True

        # Si no se cumplen las condiciones, retornamos False
        return False

    def es_valida(self, clave):
        if self.esta_repetida(clave) or self.no_cumple_con_la_cantidad_minima_de_caracteres(clave) or self.no_tiene_n_caracteres_distintos(clave, n=4):
            return False
        return True       
     
class Regla:
    def __init__(self, valor):
        self.valor = valor

    def es_valida(self):
        return self.valor > 0

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self):
        return self.regla.es_valida()

regla = Regla(1)
validador = Validador(regla)

print(validador.es_valida()) 