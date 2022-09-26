from busquedaHash import *
from Celular import Celular

def main():
    m = 500000
    T = formarTabla(m)
    obj1 = Celular("Apple", 14999)
    obj2 = Celular("Samsung", 10000)
    insertar(T, m, "Hola1", obj1)
    insertar(T, m, "Hola1", obj2)
    indice = buscar(T, m, "Hola1")
    print(T[indice])

main()