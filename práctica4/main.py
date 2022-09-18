import random
import matplotlib.pyplot as plt
from Jugador import Jugador
from generarCadena import generarCadena
from busquedaBinaria import timesBusqBinIterativaConOrdenamientoDirecto, timesBusqBinIterativaConOrdenamientoLog, timesBusqBinRecursivaConOrdenamientoDirecto, timesBusqBinRecursivaConOrdenamientoLog
from busquedaLineal import timesBusquedaLinealIterativa, timesBusquedaLinealRecursiva

MAX = 1000

"""
    Búsqueda binaria RECURSIVA con ordenamiento bubble sort
"""
# Caso promedio - Búsqueda binaria recursiva con ordenamiento bubble sort
Aax1 = []
Aax1_times = []
Aax1_elementos = []
for i in range(MAX):
    Aax1.append( Jugador(random.randint(0, 100), generarCadena(10)) )
    Aax1_times.append( timesBusqBinRecursivaConOrdenamientoDirecto(Aax1, 34, Jugador.getScore, 0, len(Aax1) - 1) )
    Aax1_elementos.append(len(Aax1))

# Mejor caso - Búsqueda binaria recursiva con ordenamiento bubble sort
Bax1 = []
Bax1_times = []
Bax1_elementos = []
for i in range(MAX):
    Bax1.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el medio => len(Bax1) // 2,
    puntoMedio = len(Bax1) // 2 - 1
    Bax1_times.append( 
        timesBusqBinRecursivaConOrdenamientoDirecto(
            Bax1, 
            Bax1[puntoMedio].getScore(), 
            Jugador.getScore, 
            0, len(Bax1) - 1 ) 
        )
    Bax1_elementos.append(len(Bax1))

# Peor caso - Búsqueda binaria recursiva con ordenamiento bubble sort
Cax1 = []
Cax1_times = []
Cax1_elementos = []
for i in range(MAX):
    Cax1.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en algún extremo => Cax1[-1].getScore()
    Cax1_times.append( 
        timesBusqBinRecursivaConOrdenamientoDirecto(
            Cax1, 
            Cax1[-1].getScore(), 
            Jugador.getScore, 
            0, len(Cax1) - 1) 
    )
    Cax1_elementos.append(len(Cax1))


"""
    Búsqueda binaria ITERATIVA con ordenamiento bubble sort
"""

# Caso promedio - Búsqueda binaria iterativa con ordenamiento bubble sort
Aax2 = []
Aax2_times = []
Aax2_elementos = []
for i in range(MAX):
    Aax2.append( Jugador(random.randint(0, 100), generarCadena(10)) )
    Aax2_times.append( timesBusqBinIterativaConOrdenamientoDirecto(Aax2, 32, Jugador.getScore) )
    Aax2_elementos.append(len(Aax2))

# Mejor caso - Búsqueda binaria iterativa con ordenamiento bubble sort
Bax2 = []
Bax2_times = []
Bax2_elementos = []
for i in range(MAX):
    Bax2.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el medio => len(Bax1) // 2,
    puntoMedio = len(Bax2) // 2 - 1
    Bax2_times.append( 
        timesBusqBinIterativaConOrdenamientoDirecto(
            Bax2, 
            Bax2[puntoMedio].getScore(), 
            Jugador.getScore )
        )
    Bax2_elementos.append(len(Bax2))

# Peor caso - Búsqueda binaria iterativa con ordenamiento bubble sort
Cax2 = []
Cax2_times = []
Cax2_elementos = []
for i in range(MAX):
    Cax2.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el último => Cax1[-1].getScore()
    Cax2_times.append( 
        timesBusqBinRecursivaConOrdenamientoDirecto(
            Cax2, 
            Cax2[-1].getScore(), 
            Jugador.getScore, 
            0, len(Cax2) - 1) 
    )
    Cax2_elementos.append(len(Cax2))

"""
    Búsqueda binaria RECURSIVA con ordenamiento merge sort
"""

# Caso promedio - Búsqueda binaria recursiva con ordenamiento merge sort
Aax3 = []
Aax3_times = []
Aax3_elementos = []
for i in range(MAX):
    Aax3.append( Jugador(random.randint(0, 100), generarCadena(10)) )
    Aax3_times.append(
        timesBusqBinRecursivaConOrdenamientoLog(
            Aax3,
            32,
            Jugador.getScore,
            0,
            len(Aax3) - 1
        )
    )
    Aax3_elementos.append(len(Aax3))

# Mejor caso - Búsqueda binaria recursiva con ordenamiento merge sort
Bax3 = []
Bax3_times = []
Bax3_elementos = []
for i in range(MAX):
    Bax3.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el medio => len(Bax3) // 2,
    puntoMedio = len(Bax3) // 2 - 1
    Bax3_times.append( 
        timesBusqBinRecursivaConOrdenamientoLog(
            Bax3,
            32,
            Jugador.getScore,
            0,
            len(Bax3) - 1
        )
    )
    Bax3_elementos.append(len(Bax3))

# Peor caso - Búsqueda binaria recursiva con ordenamiento merge sort
Cax3 = []
Cax3_times = []
Cax3_elementos = []
for i in range(MAX):
    Cax3.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el último => Cax3[-1].getScore()
    Cax3_times.append( 
        timesBusqBinRecursivaConOrdenamientoLog(
            Cax3, 
            Cax3[-1].getScore(), 
            Jugador.getScore,
            0,
            len(Cax3) - 1
        )
    )
    Cax3_elementos.append(len(Cax3))

"""
    Búsqueda binaria ITERATIVA con ordenamiento merge sort
"""

# Caso promedio - Búsqueda binaria iterativa con ordenamiento merge sort
Aax4 = []
Aax4_times = []
Aax4_elementos = []
for i in range(MAX):
    Aax4.append( Jugador(random.randint(0, 100), generarCadena(10)) )
    Aax4_times.append(
        timesBusqBinIterativaConOrdenamientoLog(
            Aax4,
            32,
            Jugador.getScore
        )
    )
    Aax4_elementos.append(len(Aax4))

# Mejor caso - Búsqueda binaria recursiva con ordenamiento merge sort
Bax4 = []
Bax4_times = []
Bax4_elementos = []
for i in range(MAX):
    Bax4.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el medio => len(Bax3) // 2,
    puntoMedio = len(Bax4) // 2 - 1
    Bax4_times.append( 
        timesBusqBinIterativaConOrdenamientoLog(
            Bax4,
            Bax4[puntoMedio].getScore(),
            Jugador.getScore
        )
    )
    Bax4_elementos.append(len(Bax4))

# Peor caso - Búsqueda binaria recursiva con ordenamiento merge sort
Cax4 = []
Cax4_times = []
Cax4_elementos = []
for i in range(MAX):
    Cax4.append( Jugador(i, generarCadena(10)) )
    # Búscando el elemento que está en el último => Cax3[-1].getScore()
    Cax4_times.append( 
        timesBusqBinIterativaConOrdenamientoLog(
            Cax4,
            Cax4[-1].getScore(),
            Jugador.getScore
        )
    )
    Cax4_elementos.append(len(Cax4))

"""
    Búsqueda lineal iterativa
"""
# Caso promedio
Aax5 = []
Aax5_times = []
Aax5_elementos = []
for i in range(MAX):
    Aax5.append( Jugador(i, generarCadena(10)) )
    x, times = timesBusquedaLinealIterativa(Aax5, Jugador.getScore, random.randint(0, 100))
    Aax5_times.append( times )
    Aax5_elementos.append(len(Aax5))

# Mejor caso
Bax5 = []
Bax5_times = []
Bax5_elementos = []
for i in range(MAX):
    Bax5.append( Jugador(random.randint(0, 100), generarCadena(10)) )
    # Búscando el primer elemento
    x, times = timesBusquedaLinealIterativa(Bax5, Jugador.getScore, Bax5[0].getScore())
    Bax5_times.append( times )
    Bax5_elementos.append(len(Bax5))

# Peor caso
Cax5 = []
Cax5_times = []
Cax5_elementos = []
for i in range(MAX):
    Cax5.append( Jugador(i, generarCadena(10)) )
    # Búscando el último elemento
    x, times = timesBusquedaLinealIterativa(Cax5, Jugador.getScore, i)
    Cax5_times.append( times )
    Cax5_elementos.append(len(Cax5))

"""
    Búsqueda lineal recursiva
"""
# Caso promedio
Aax6 = []
Aax6_times = []
Aax6_elementos = []
for i in range(MAX):
    Aax6.append( Jugador(i, generarCadena(10)) )
    x, times = timesBusquedaLinealRecursiva(Aax6, Jugador.getScore, random.randint(0, 100), 0)
    Aax6_times.append( times )
    Aax6_elementos.append(len(Aax6))

# Mejor caso
Bax6 = []
Bax6_times = []
Bax6_elementos = []
for i in range(MAX):
    Bax6.append( Jugador(random.randint(0, 100), generarCadena(10)) )
    # Búscando el primer elemento
    x, times = timesBusquedaLinealRecursiva(Bax6, Jugador.getScore, Bax6[0].getScore(), 0)
    Bax6_times.append( times )
    Bax6_elementos.append(len(Bax6))

# Peor caso
Cax6 = []
Cax6_times = []
Cax6_elementos = []
for i in range(MAX):
    Cax6.append( Jugador(i, generarCadena(10)) )
    # Búscando el último elemento
    x, times = timesBusquedaLinealRecursiva(Cax6, Jugador.getScore, i, 0)
    Cax6_times.append( times )
    Cax6_elementos.append(len(Cax6))



# Construyendo gráfica...
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(100, 60))
ax1, ax2, ax3, ax4, ax5 ,ax6 = axes.flatten()
fig.subplots_adjust(hspace=0.5)


ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax5.grid(True)
ax6.grid(True)

ax1.set_title("Búsq. bin. recursiva con ord. bubble sort")
ax1.plot(Aax1_times, Aax1_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax1.plot(Bax1_times, Bax1_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax1.plot(Cax1_times, Cax1_elementos, label = 'Peor caso', marker = 'x', color = 'r')

ax2.set_title("Búsq. bin. iterativa con ord. bubble sort")
ax2.plot(Aax2_times, Aax2_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax2.plot(Bax2_times, Bax2_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax2.plot(Cax2_times, Cax2_elementos, label = 'Peor caso', marker = 'x', color = 'r')

ax3.set_title("Búsq. bin. recursiva con ord. merge sort")
ax3.plot(Aax3_times, Aax3_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax3.plot(Bax3_times, Bax3_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax3.plot(Cax3_times, Cax3_elementos, label = 'Peor caso', marker = 'x', color = 'r')

ax4.set_title("Búsq. bin. iterativa con ord. merge sort")
ax4.plot(Aax4_times, Aax4_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax4.plot(Bax4_times, Bax4_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax4.plot(Cax4_times, Cax4_elementos, label = 'Peor caso', marker = 'x', color = 'r')

ax5.set_title("Búsq. lineal iterativa")
ax5.plot(Aax5_times, Aax5_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax5.plot(Bax5_times, Bax5_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax5.plot(Cax5_times, Cax5_elementos, label = 'Peor caso', marker = 'x', color = 'r')

ax6.set_title("Búsq. lineal recursiva")
ax6.plot(Aax6_times, Aax6_elementos, label = 'Caso promedio', marker = '*', color = 'b')
ax6.plot(Bax6_times, Bax6_elementos, label = 'Mejor caso', marker = 'o', color = 'g')
ax6.plot(Cax6_times, Cax6_elementos, label = 'Peor caso', marker = 'x', color = 'r')


# Labels de gráficas
ax1.set_xlabel('Veces que entra')
ax1.set_ylabel('Elementos')
ax1.legend(loc=2)

ax2.set_xlabel('Veces que entra')
ax2.set_ylabel('Elementos')
ax2.legend(loc=2)

ax3.set_xlabel('Veces que entra')
ax3.set_ylabel('Elementos')
ax3.legend(loc=2)

ax4.set_xlabel('Veces que entra')
ax4.set_ylabel('Elementos')
ax4.legend(loc=2)

ax5.set_xlabel('Veces que entra')
ax5.set_ylabel('Elementos')
ax5.legend(loc=2)

ax6.set_xlabel('Veces que entra')
ax6.set_ylabel('Elementos')
ax6.legend(loc=2)


plt.show()