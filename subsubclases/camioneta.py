from subclases import coche
class Camioneta(coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return f"{super().__str()}, {self.carga} kg"
    def __name__(self):
        return "Camioneta"