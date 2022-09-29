
def formarTablaAnidada(longitud):
    return [ [] for _ in range(longitud) ]

"""
    Implemetación con listas enlazadas
"""

def hashModulo(llave, longitud):

    llaveConvertida = convertirLLave(str(llave))

    return llaveConvertida % longitud


def convertirLLave(llave):
    keyNum = 0

    for char in llave:
        keyNum = keyNum + ord(char)
        
    return keyNum


def insertarLineal(tabla, llave, valor):

    indice = hashModulo(llave, len(tabla))
    llaveValor = [llave, valor]
    tabla[indice].append(llaveValor)


def buscarLineal(tabla, llave):

    indice = hashModulo(llave, len(tabla))
    
    i = 0
    while i < len(tabla[indice]):
        
        if tabla[indice][i][0] == llave:
            return tabla[indice][i][1] # retornando valor de la llave
        
        i = i + 1
    
    return False


"""
    Funciones para contar
"""

def timesConvertirLlave(llave):
    times = 0

    keyNum = 0
    for char in llave:
        times += 1
        keyNum = keyNum + ord(char)
        
    return keyNum, times


def timesHashModulo(llave, longitud):

    times = 0

    llaveConvertida, time = timesConvertirLlave(str(llave))

    times += time

    return llaveConvertida % longitud, times


def timesInsertarLineal(tabla, llave, valor):
    times = 0

    indice, time = timesHashModulo(llave, len(tabla))

    times += time

    llaveValor = [llave, valor]
    tabla[indice].append(llaveValor)

    return times


def timesBuscarLineal(tabla, llave):
    times = 0

    indice, time = timesHashModulo(llave, len(tabla))

    times += time
    

    i = 0 # Tratando posibles colisiones
    while i < len(tabla[indice]):
        times += 1
        
        if tabla[indice][i][0] == llave:
            return tabla[indice][i][1], times # retornando valor de la llave
        
        i = i + 1
    
    return False, times