
def formarTabla(longitud):
    T = [None] * longitud
    return T


def convertirLLave(llave):
    keyNum = 0
    i = 0
    for char in llave:
        keyNum = keyNum + ord(char) * i
        i = i + 1

    return keyNum

def hash(llave, longitud):
    return llave % longitud

def insertar(T, longitud, llave, valor):

    h1 = hash(convertirLLave(llave), longitud)

    j = 0
    while j < longitud:

        indice = (h1 + j) % longitud
        llaveValor = [llave, valor]

        if  T[indice] == None:
            T[indice] = llaveValor
            return indice
        
        else:
            j = j + 1
        
    print("No hay lugar")

    return -1

def buscar(T, longitud, llave):

    h1 = hash(convertirLLave(llave), longitud)

    j = 0
    while j < longitud:
    
        indice = (h1 + j) % longitud

        if T[indice] != None and T[indice][0] == llave:
            return indice
        else:
            j = j + 1

        return -1

    return -1


def timesConvertirLLave(llave):
    times = 0
    times += 1

    keyNum = 0
    i = 0
    for char in llave:
        times += 1

        keyNum = keyNum + ord(char) * i
        i = i + 1

    return keyNum, times

def timesInsertar(T, longitud, llave, valor):

    times = 0
    times += 1

    llaveConv, time = timesConvertirLLave(llave)

    times += time

    h1 = hash(llaveConv, longitud)

    j = 0
    while j < longitud:

        times += 1

        indice = (h1 + j) % longitud
        llaveValor = [llave, valor]

        if  T[indice] == None:
            T[indice] = llaveValor
            return indice, times
        else:
            j = j + 1
        
    print("No hay lugar")

    return -1, times

def timesBuscar(T, longitud, llave):

    times = 0
    times += 1

    llaveConv, time = timesConvertirLLave(llave)
    h1 = hash(llaveConv, longitud)
    times += time

    j = 0
    while j < longitud:

        times += 1
    
        indice = (h1 + j) % longitud

        if T[indice] != None and T[indice][0] == llave:
            return indice, times
        else:
            j = j + 1

        return -1, times

    return -1, times