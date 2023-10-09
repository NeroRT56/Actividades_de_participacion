from AP8.tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __init__(self, libro: Libro):
        super().__init__(libro)

    pass
    # Defina metodo inicializador

    # Defina metodo especial
