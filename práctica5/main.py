import random
import matplotlib.pyplot as plt

from generarCadena import generarCadena

from busquedaHash import *
from Celular import Celular


def main():

    MAX = 1000

    A_elementos = []
    A_times = []
    A = formarTabla(MAX)
    for i in range(1, MAX):
        A_elementos.append(i)

        times = 0
        cadena = generarCadena( 10 )
        x, time = timesInsertar(
            A, i, 
            cadena, 
            Celular( cadena, random.randint( 1, 20000 ) )
        )
        times += time

        x, time = timesBuscar(A, i, cadena)
        times += time
        
        A_times.append(times)


    C_elementos = []
    C_times = []
    C = formarTabla(MAX)
    for i in range(1, MAX):
        C_elementos.append(i)
        
        llave = "repetida"
        times = 0
        x, time = timesInsertar(
            C, i, llave, # Usando misma llave 
            Celular( generarCadena(10), random.randint( 1, 20000 ) )
        )
        times += time

        x, time = timesBuscar(A, i, llave)
        times += time
        C_times.append(times)


    # Construyendo gráfica...
    fig, ax = plt.subplots()
    ax.plot(A_elementos, A_times, label='Caso promedio', marker='*', color='b')
    # ax.plot([], [], label='Mejor caso', marker='o', color='g')
    ax.plot(C_elementos, C_times, label='Peor caso', marker='x', color='r')
    plt.title('Búsqueda Hash')
    ax.set_xlabel('Elementos')
    ax.set_ylabel('Veces que entra')
    ax.grid(True)
    ax.legend(loc=2)
    plt.show()



main()
