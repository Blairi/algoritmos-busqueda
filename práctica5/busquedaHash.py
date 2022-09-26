
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

def h(llave, longitud):
    return llave % longitud

def insertar(T, longitud, llave, valor):

    h1 = h(convertirLLave(llave), longitud)

    j = 0
    while j < longitud:

        indice = (h1 + j) % longitud
        llaveValor = [llave, valor]

        if T[indice] != None and T[indice][0] == llave: # Si ya existe la llave, reasignamos el nuevo valor
            T[indice] = llaveValor
            return indice

        if  T[indice] == None:
            T[indice] = llaveValor
            return indice
        
        j = j + 1
        
    print("No hay lugar")
    return -1

def buscar(T, longitud, llave):

    h1 = h(convertirLLave(llave), longitud)

    j = 0
    while j < longitud:
    
        indice = (h1 + j) % longitud

        if T[indice] != None and T[indice][0] == llave:
            return indice
        else:
            j = j + 1

        return -1

    return -1

# def buscar(T, longitud, llave):

#     h1 = h(convertirLLave(llave), longitud)

#     j = 0
#     while j < longitud:
#         indice = (h1 + j) % longitud

#         if T[indice] != None:
            
#             if T[indice][0] == llave:
#                 return indice
#             else:
#                 j = j + 1

#         return -1

#     return -1