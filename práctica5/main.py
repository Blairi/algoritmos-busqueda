import random
import matplotlib.pyplot as plt

from busquedaHashAnidada import formarTablaAnidada, insertarLineal, timesBuscarLineal, timesInsertarLineal
from Celular import Celular

from generarCadena import generarCadena
from recorrerLetras import recorrerLetra

def verLista(lista):
    for listaAni in lista:
        print(listaAni)

MAX = 100

"""
    Búsqueda Hash anidada
"""

# Caso promedio al insertar
tPromedioAni = formarTablaAnidada(MAX)
insertarPromedioElementosAni = []
insertarPromedioTimesAni = []
for i in range(1, MAX + 1):

    times = timesInsertarLineal(
        tPromedioAni, 
        generarCadena(random.randint(1, 10)), 
        Celular( generarCadena(7), random.randint(1, 1500) )
    )
    
    insertarPromedioElementosAni.append(i)
    insertarPromedioTimesAni.append(times)

# Caso promedio al buscar
tPromedioAni = formarTablaAnidada(MAX)
buscarPromedioElementosAni = []
buscarPromedioTimesAni = []
for i in range(1, MAX + 1):
    
    # Insertando y guardando la llave
    llaveAleatoria = generarCadena(random.randint(1, 10))
    insertarLineal(
        tPromedioAni,
        llaveAleatoria,
        Celular( generarCadena(7), random.randint(1, 1500) )
    )

    # Búscamos la llave generada
    x, times = timesBuscarLineal(tPromedioAni, llaveAleatoria)
    buscarPromedioElementosAni.append(i)
    buscarPromedioTimesAni.append(times)


# Mejor caso al insertar
tMejorAni = formarTablaAnidada(MAX)
insertarMejorElementosAni = []
insertarMejorTimesAni = []
cuenta = 0
for i in range(1, MAX + 1):
    mejorLlave = ""
    if cuenta < 256:
        mejorLlave = chr(i) # Generamos el caracter ascii diferente
        cuenta += 1
    else:
        mejorLlave = ""
        cuenta = 0

    times = timesInsertarLineal(
        tMejorAni,
        mejorLlave,
        Celular( generarCadena(7), random.randint(1, 1500) )
    )
    insertarMejorElementosAni.append(i)
    insertarMejorTimesAni.append(times)

# Mejor caso al buscar
tMejorAni = formarTablaAnidada(MAX)
buscarMejorElementosAni = []
buscarMejorTimesAni = []
cuenta = 0
for i in range(1, MAX + 1):

    mejorLlave = ""
    if cuenta < 256:
        mejorLlave = chr(i) # Generamos el caracter ascii diferente
        cuenta += 1
    else:
        mejorLlave = ""
        cuenta = 0
    
    insertarLineal(
        tMejorAni,
        mejorLlave,
        Celular( generarCadena(7), random.randint(1, 1500) )
    )
    x, times = timesBuscarLineal(tMejorAni, mejorLlave)
    buscarMejorElementosAni.append(i)
    buscarMejorTimesAni.append(times)


# Peor caso al insertar
llaveRepetida = "repetida"

tPeorAni = formarTablaAnidada(MAX)
insertarPeorElementosAni = []
insertarPeorTimesAni = []
for i in range(1, MAX + 1):
    times = timesInsertarLineal(
        tPeorAni, 
        llaveRepetida,
        Celular( generarCadena(7), random.randint(1, 1500) )
    )
    insertarPeorElementosAni.append(i)
    insertarPeorTimesAni.append(times)

# Peor caso al buscar
tPeorAni = formarTablaAnidada(MAX)
buscarPeorElementosAni = []
buscarPeorTimesAni = []
cadena = generarCadena(MAX)
for i in range(1, MAX + 1):
    
    # Búscamos la misma llave solo que ordenada de distinta manera
    llaveRepetida = recorrerLetra(cadena, i)

    insertarLineal(
        tPeorAni, 
        llaveRepetida, 
        Celular( generarCadena(7), random.randint(1, 1500) )
    )

    x, times = timesBuscarLineal(tPeorAni, llaveRepetida)

    buscarPeorElementosAni.append(i)
    buscarPeorTimesAni.append(times)


# Construyendo gráfica...
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(100, 60))
ax1, ax2, ax3, ax4 = axes.flatten()
fig.subplots_adjust(hspace=0.5)

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)


ax1.set_title("Insersión búsq. hash anidada")
ax1.plot(insertarPromedioElementosAni, insertarPromedioTimesAni, label = 'Caso promedio', marker = '*', color = 'b')
ax1.plot(insertarMejorElementosAni, insertarMejorTimesAni, label = 'Mejor caso', marker = 'o', color = 'g')
ax1.plot(insertarPeorElementosAni, insertarPeorTimesAni, label = 'Peor caso', marker = 'x', color = 'r')

ax2.set_title("Búsqueda hash anidada")
ax2.plot(buscarPromedioElementosAni, buscarPromedioTimesAni, label = 'Caso promedio', marker = '*', color = 'b')
ax2.plot(buscarMejorElementosAni, buscarMejorTimesAni, label = 'Mejor caso', marker = 'o', color = 'g')
ax2.plot(buscarPeorElementosAni, buscarPeorTimesAni, label = 'Peor caso', marker = 'x', color = 'r')

# Labels de gráficas
ax1.set_ylabel('Veces que entra')
ax1.set_xlabel('Elementos insertados')
ax1.legend(loc=2)

ax2.set_ylabel('Veces que entra')
ax2.set_xlabel('Elementos insertados')
ax2.legend(loc=2)

ax3.set_ylabel('Veces que entra')
ax3.set_xlabel('Elementos insertados')
ax3.legend(loc=2)

ax4.set_ylabel('Veces que entra')
ax4.set_xlabel('Elementos insertados')
ax4.legend(loc=2)

plt.show()
