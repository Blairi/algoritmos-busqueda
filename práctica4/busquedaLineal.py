from Jugador import Jugador

def busquedaLinealIterativa(A, attr, key):
    for i in range(len(A)):
        if key == attr(A[i]):
            return i
    return False

def timesBusquedaLinealIterativa(A, attr, key):
    times = 0
    for i in range(len(A)):
        times += 1
        if key == attr(A[i]):
            return i, times
    return False, times


def busquedaLinealRecursiva(A, attr, key, indice):

    if indice >= len(A):
        return False

    if key == attr(A[indice]):
        return indice

    indice = indice + 1

    return busquedaLinealRecursiva(A, attr, key, indice)

def timesBusquedaLinealRecursiva(A, attr, key, indice):

    times = 0
    times += 1

    if indice >= len(A):
        return False, times

    if key == attr(A[indice]):
        return indice, times

    indice = indice + 1

    ret, time = timesBusquedaLinealRecursiva(A, attr, key, indice)
    times += time
    return ret, times


# Prueba con contador
# A = []
# for i in range(10):
#    A.append(Jugador(i * 3, "Pedro"))

# for jugador in A:
#     print(jugador)

# x, times = timesBusquedaLinealIterativa(A, Jugador.getScore, 27)
# print(f"Se tardo {times} en encontrar {x}")

# x, times = timesBusquedaLinealRecursiva(A, Jugador.getScore, 27, 0)
# print(f"Se tardo {times} en encontrar {x}")



# Prueba
# A = []
# for i in range(10):
#    A.append(Jugador(i * 3, "Pedro"))

# for jugador in A:
#     print(jugador)

# print(busquedaLinealIterativa(A, Jugador.getScore, 6))
# print(busquedaLinealRecursiva(A, Jugador.getScore, 27, 0))

