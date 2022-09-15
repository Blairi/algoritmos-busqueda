from Jugador import Jugador

def busquedaLinealIterativa(A, attr, key):
    for i in range(len(A)):
        if key == attr(A[i]):
            return i
    return False

def busquedaLinealRecursiva(A, attr, key, indice):

    if indice >= len(A) - 1:
        return False

    if key == attr(A[indice]):
        return indice

    indice = indice + 1

    return busquedaLinealRecursiva(A, attr, key, indice)


# A = []
# for i in range(10):
   # A.append(Jugador(i * 3, "Pedro"))

# for jugador in A:
    # print(jugador)

# print(busquedaLinealIterativa(A, Jugador.getScore, 6))
# print(busquedaLinealRecursiva(A, Jugador.getScore, 6, 0))

