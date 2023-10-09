class CarroCompras:
    def __init__(self):
        self.item = []
    def agregar_item(self,libro, cantidad):
        item = self.item(libro, cantidad)
        self.items.append(item)
        return item 
    def calcular_total(self):
        total = 0
        for item in self.items:
            subtotal = item.calcular_subtotal()
            total += subtotal
        return total
    def quitar_item(self, isbn):
        self.item= [item for item in self. items if item.libro.isbn != isbn]

    pass
    # Defina metodo inicializador __init__(self)

    # Defina el metodo agregar_item

    # Defina el metodo calcular_total

    # Defina el metodo quitar_item
