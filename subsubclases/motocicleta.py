from subclases import bicicleta
class Motocicleta(bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return f"{super().__str()}, {self.velocidad} km/h, {self.cilindrada} cc"
    def __name__(self):
        return "Motocicleta"