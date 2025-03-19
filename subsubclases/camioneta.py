from subclases.coche import Coche
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return f"{super().__str__()}, {self.carga} kg"
    def __name__(self):
        return "Camioneta"