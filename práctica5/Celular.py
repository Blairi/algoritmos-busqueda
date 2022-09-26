
class Celular:
    
    marca = None
    precio = None

    def __init__(self, marca, precio) -> None:
        self.marca = marca
        self.precio = precio

    def __str__(self) -> str:
        return f"marca: {self.marca}\nprecio: {self.precio}"
    
    def getMarca(self) -> str:
        return self.marca

    def getPrecio(self) -> int:
        return self.precio