from carro_compra import CarroCompras
from libro_existente_error import LibroExistenteError
from AP8.tiendalibros.modelo.libro import Libro
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
     def __init__(self):
        self.catálogo = {}
        self.carrito = CarroCompras()
     def adicionar_libro_a_catálogo(self, isbn: str, titulo: str, precio:float , existencias: int):
        if isbn in self.catálogo:
            raise LibroExistenteError("El libro ya existe en el catálogo")
        else:
            libro = Libro(isbn, titulo, precio, existencias)
            self.catálogo[isbn] = libro
            return libro
    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo
     def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        elif libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn)
        else:
            self.carrito.agregar_item(libro, cantidad)
     def retirar_item_de_carrito(self, isbn):
         self.carrito.quitar_item(isbn)
         
         
    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
