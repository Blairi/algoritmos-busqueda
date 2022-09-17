from Jugador import Jugador
import random

def bubbleSort( A, attr ):
    for _ in range( 1, len( A ) + 1 ):
        for j in range( len( A ) - 1 ):
            if attr(A[j]) > attr(A[j + 1]):
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

def timesBubbleSort( A, attr ):
    times = 0
    for _ in range( 1, len( A ) + 1 ):
        times += 1
        for j in range( len(A) - 1 ):
            times += 1
            if attr(A[j]) > attr(A[j + 1]):
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

    return times

# A = []
# for i in range(10):
#     A.append(Jugador(random.randint(0, 100), "pedro"))

# for jugador in A:
#     print(jugador)

# print()

# bubbleSort(A, Jugador.getScore)
# print(timesBubbleSort(A, Jugador.getScore))

# for jugador in A:
#     print(jugador)