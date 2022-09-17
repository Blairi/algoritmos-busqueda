from Jugador import Jugador
import random

def crearSubArreglo(A, indIzq, indDer):
    return A[indIzq:indDer + 1]

def merge(A, attr, p, q, r):
    izq = crearSubArreglo( A, p, q )
    der = crearSubArreglo( A, q + 1, r )

    i = 0
    j = 0
    for k in range( p, r + 1 ):
        if ( j >= len( der ) ) or ( i < len( izq ) and attr(izq[i]) < attr(der[j]) ):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1

def mergeSort(A, attr, p, r):
    if r - p > 0:
        q = int( (p + r) / 2 )
        mergeSort( A, attr, p, q )
        mergeSort( A, attr, q + 1, r )
        merge( A, attr, p, q, r )
        return A


def timesMerge(A, attr, p, q, r):

    times = 0

    izq = crearSubArreglo( A, p, q )
    der = crearSubArreglo( A, q + 1, r )

    i = 0
    j = 0
    for k in range( p, r + 1 ):
        times += 1
        if ( j >= len( der ) ) or ( i < len( izq ) and attr(izq[i]) < attr(der[j]) ):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1

    return times

def timesMergeSort(A, attr, p, r):
    times = 0
    if r - p > 0:
        q = int( (p + r) / 2 )
        times += timesMergeSort( A, attr, p, q )
        times += timesMergeSort( A, attr, q + 1, r )
        times += timesMerge( A, attr, p, q, r )
    return times


# A = []
# for i in range(10):
#     A.append(Jugador(random.randint(0, 100), "pedro"))

# for jugador in A:
#     print(jugador)

# print()

# mergeSort(A, Jugador.getScore, 0, len(A) - 1)
# print(timesMergeSort(A, Jugador.getScore, 0, len(A) - 1))

# for jugador in A:
#     print(jugador)