#P cree un método depositar que maneje las acciones de depósito en la cuenta.
#P cree un método retirar que maneje las acciones de retiro de la cuenta.
#P,cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#P cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class Cuenta_bancaria:
    def __init__(self, numero_de_cuenta, propietarios, balance):
        self.numero_de_cuenta = numero_de_cuenta
        self.propietarios = propietarios
        self.balance = balance
    def depositar (self, cantidad):
        self.balance += cantidad
    def retirar (self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else :
            print("Tienes fondos insuficientes")
    def Cuota_manejo(self):
        
        intereses = self.balance * 0.02
        self.balance -= intereses
    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print("Número de cuenta:", self.numero_de_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)
cuenta = Cuenta_bancaria("123456789", ["Juan Perez", "Maria Gomez"], 1000.0)       

cuenta.depositar(500.0)
cuenta.retirar(200.0)
cuenta.Cuota_manejo()
cuenta.mostrar_detalles()