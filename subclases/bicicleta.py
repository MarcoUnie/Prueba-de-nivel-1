from superclases import vehiculo
class Bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"{super().__str()}, {self.tipo}"
    def __name__(self):
        return "Bicicleta"