from Jugador import Jugador

def busquedaBinariaIterativa(A, key, attr):
    i = 0
    f = len( A ) - 1

    while f >= i:
        m = ( f + i ) // 2
        if attr(A[m]) == key:
            return m

        if attr(A[m]) > key:
            f = m - 1
        else:
            i = m + 1
    return False

def busquedaBinariaRecursiva(A, key, attr, inicio, final):
    if inicio > final:
        return False

    m = (inicio + final) // 2

    if attr(A[m]) == key:
        return m

    if attr(A[m]) > key:
        return busquedaBinariaRecursiva(A, key, attr, inicio, m - 1)

    else:
        return busquedaBinariaRecursiva(A, key, attr, m + 1, final)

# A = []
# for i in range(10):
    # A.append(Jugador(i * 3, "Pedro"))

# for jugador in A:
    # print(jugador)

# print(busquedaBinariaRecursiva(A, 27, Jugador.getScore, 0, len(A) - 1))
# print(busquedaBinariaIterativa(A, 27, Jugador.getScore))

