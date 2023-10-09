from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro import Libro


class LibroAgotadoError(LibroError):
    def __init__(self,libro:Libro):
         super().__init__(libro)

    def __str__(self) -> str:
        return  f"El libro con titulo {self.titulo} y isbn {self.isbn} esta agotado"
   

    # Defina metodo inicializador

    # Defina metodo especial
