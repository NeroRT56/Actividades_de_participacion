class ValidadorError(Exception):
    def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=3)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True


class NoCumpleLongitudMinimaError(ValidadorError):
    def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=4)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True


class NoTieneLetraMayusculaError(ValidadorError):
    def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=4)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True


class NoTieneLetraMinusculaError(ValidadorError):
   def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=4)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True

class NoTieneNumeroError(ValidadorError):
    def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=4)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True



class NoTieneCaracterEspecialError(ValidadorError):
    def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=4)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True


class NoTienePalabraSecretaError(ValidadorError):
    def es_valida(self, clave):
        try:
            self.esta_repetida(clave)
            self.no_cumple_con_la_cantidad_minima_de_caracteres(clave)
            self.no_tiene_n_caracteres_distintos(clave, n=4)
        except (Regla1Excepcion, Regla2Excepcion,
                Regla3Excepcion, Regla4Excepcion):
            return False
        return True