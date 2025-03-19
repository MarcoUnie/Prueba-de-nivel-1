from superclases import vehiculo
class Coche(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return f"{super().__str()}, {self.velocidad} km/h, {self.cilindrada} cc"
    def __name__(self):
        return "Coche"