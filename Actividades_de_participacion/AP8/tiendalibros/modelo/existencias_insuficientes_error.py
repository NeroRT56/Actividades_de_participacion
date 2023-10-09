from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __str__(self) -> str:
        return f" El libro con titulo {self.titulo} y {self.libro} no tiene suficientes existencias para realizar la compra: cantidad a comprar:{self.cantidad},existencia{self.libro.existencias}"
    

    # Defina metodo inicializador

    # Defina metodo espcial
