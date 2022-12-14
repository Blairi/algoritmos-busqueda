import random
from Jugador import Jugador
from bubbleSort import timesBubbleSort
from mergeSort import timesMergeSort

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


def timesBusquedaBinariaIterativa(A, key, attr):

    times = 0

    i = 0
    f = len( A ) - 1

    while f >= i:

        times += 1

        m = ( f + i ) // 2
        if attr(A[m]) == key:
            return m, times

        if attr(A[m]) > key:
            f = m - 1
        else:
            i = m + 1

    return False, times


def timesBusqBinIterativaConOrdenamientoDirecto(A, key, attr):
    times = 0
    times += timesBubbleSort(A, attr)
    x, time = timesBusquedaBinariaIterativa(A, key, attr)
    times += time
    return times


def timesBusqBinIterativaConOrdenamientoLog(A, key, attr):
    times = 0
    times += timesMergeSort(A, attr, 0, len(A) - 1)
    x, time = timesBusquedaBinariaIterativa(A, key, attr)
    times += time
    return times


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
        

def timesBusquedaBinariaRecursiva(A, key, attr, inicio, final):

    times = 0
    times += 1

    if inicio > final:
        return False, times

    m = (inicio + final) // 2
    
    if attr(A[m]) == key:
        return m, times

    if attr(A[m]) > key:
        ret, time = timesBusquedaBinariaRecursiva(A, key, attr, inicio, m - 1)
        times += time
        return ret, times

    else:
        ret, time = timesBusquedaBinariaRecursiva(A, key, attr, m + 1, final)
        times += time
        return ret, times
    

def timesBusqBinRecursivaConOrdenamientoDirecto(A, key, attr, inicio, final):
    times = 0
    times += timesBubbleSort(A, attr) # ordenando ...
    x,time = timesBusquedaBinariaRecursiva(A, key, attr, inicio, final)
    times += time
    return times


def timesBusqBinRecursivaConOrdenamientoLog(A, key, attr, inicio, final):
    times = 0
    times += timesMergeSort(A, attr, inicio, final) # ordenando ...
    x,time = timesBusquedaBinariaRecursiva(A, key, attr, inicio, final)
    times += time
    return times



# Pruebas iterativas con ordenamiento merge sort
# A = []
# for _ in range(10):
#     A.append(Jugador(random.randint(0, 100), "Pedro"))
# for jugador in A:
#     print(jugador)
# tiempo = timesBusqBinIterativaConOrdenamientoLog(A, 2, Jugador.getScore)
# print(tiempo)

# Pruebas iterativas con ordenamiento bubble sort
# A = []
# for _ in range(10):
#     A.append(Jugador(random.randint(0, 100), "Pedro"))
# for jugador in A:
#     print(jugador)
# tiempo = timesBusqBinIterativaConOrdenamientoDirecto(A, 2, Jugador.getScore)
# print(tiempo)



# Pruebas recursivas con ordenamiento bubble sort
# A = []
# for _ in range(10):
#     A.append(Jugador(random.randint(0, 100), "Pedro"))
# for jugador in A:
#     print(jugador)
# tiempo = timesBusqBinRecursivaConOrdenamientoDirecto(A, 2, Jugador.getScore, 0, len(A) - 1)
# print(tiempo)

# Pruebas recursivas con ordenamiento merge sort
# A = []
# for _ in range(10):
#     A.append(Jugador(random.randint(0, 100), "Pedro"))
# for jugador in A:
#     print(jugador)
# tiempo = timesBusqBinRecursivaConOrdenamientoLog(A, 1, Jugador.getScore, 0, len(A) - 1)
# print(tiempo)




# Prueba con contador
# A = []
# for i in range(10):
#     A.append(Jugador(i * 3, "Pedro"))

# for jugador in A:
#     print(jugador)

# x, times = timesBusquedaBinariaIterativa(A, 12, Jugador.getScore)
# print(f"Se tardo {times} en encontrar {x}")

# x, times = timesBusquedaBinariaRecursiva(A, 9, Jugador.getScore, 0, len(A) - 1)
# print(f"Se tardo {times} en encontrar {x}")


# Prueba
# A = []
# for i in range(10):
    # A.append(Jugador(i * 3, "Pedro"))

# for jugador in A:
    # print(jugador)

# print(busquedaBinariaRecursiva(A, 27, Jugador.getScore, 0, len(A) - 1))
# print(busquedaBinariaIterativa(A, 27, Jugador.getScore))

