class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mostrar_info(self):
        return f"{self.marca} {self.modelo}"
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def mostrar_info(self):
        return f"{super().mostrar_info()} con {self.puertas} puertas"
# Uso
coche = Coche("Toyota", "Corolla", 4)
print(coche.mostrar_info())  # Toyota Corolla con 4 puertas