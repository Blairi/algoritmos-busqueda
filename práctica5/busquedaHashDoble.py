
def formarTablaVacia(longitud):
    return [ None for _ in range(longitud) ]


"""
    Implementación con doble dirección hash
"""

def convertirLLaveV2(llave):
    suma = 0
    pos = 1
    for char in llave:
        # Sumando y multiplicando por la posición
        suma = suma + ord(char) * pos
        pos = pos + 1
    
    return suma
    
def hashModulo(llave, longitud):

    llaveConvertida = convertirLLaveV2(str(llave))
    return llaveConvertida % longitud

def insertarHashDoble(tabla, llave, valor):
    indice = hashModulo(llave, len(tabla))
    llaveValor = [llave, valor]
    
    i = 0
    while i < len(tabla):

        if tabla[indice] == None:
            tabla[indice] = llaveValor
            return True

        else: # Si ya éxiste volvemos a hashear hasta encontrar uno vacío
            indice = hashModulo(indice, len(tabla))
        
        i = i + 1 # Asegurando que si no existe un lugar vacío romper el ciclo

    return False

def buscarHashDoble(tabla, llave):
    indice = hashModulo(llave, len(tabla))
    i = 0
    while i < len(tabla):

        if tabla[indice][0] == llave:
            return tabla[indice][1]

        else: # Si ya éxiste volvemos a hashear hasta encontrar uno vacío
            indice = hashModulo(indice, len(tabla))
        
        i = i + 1 # Asegurando que si no existe un lugar vacío romper el ciclo

    return False

"""
    Funciones para contar
"""

def timesConvertirLLaveV2(llave):
    times = 0

    suma = 0
    pos = 1
    for char in llave:
        times += 1

        # Sumando y multiplicando por la posición
        suma = suma + ord(char) * pos
        pos = pos + 1
    
    return suma, times

def timesHashModulo(llave, longitud):

    llaveConvertida, times = timesConvertirLLaveV2(str(llave))
    return llaveConvertida % longitud, times

def timesInsertarHashDoble(tabla, llave, valor):
    times = 0

    indice, time = timesHashModulo(llave, len(tabla))
    times += time

    llaveValor = [llave, valor]
    
    i = 0
    while i < len(tabla):
        times += 1

        if tabla[indice] == None:
            tabla[indice] = llaveValor
            return times

        else: # Si ya éxiste volvemos a hashear hasta encontrar uno vacío
            indice, time = timesHashModulo(indice, len(tabla))
            times += time
        
        i = i + 1 # Asegurando que si no existe un lugar vacío romper el ciclo

    return times

def timesBuscarHashDoble(tabla, llave):
    times = 0

    indice, time = timesHashModulo(llave, len(tabla))
    times += time

    i = 0
    while i < len(tabla):
        times += 1

        if tabla[indice][0] == llave:
            return tabla[indice][1], times

        else: # Si ya éxiste volvemos a hashear hasta encontrar uno vacío
            indice, time = timesHashModulo(indice, len(tabla))
            times += time
        
        i = i + 1 # Asegurando que si no existe un lugar vacío romper el ciclo

    return False, times
