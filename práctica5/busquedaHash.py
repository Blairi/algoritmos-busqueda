
def formarTabla(m):
    T = [None] * m
    return T


def convertirLLave(x):
    keyNum = 0
    i = 0

    for char in x:
        keyNum = keyNum + ord(char) * i
        i = i + 1

    return keyNum

def h(x, m):
    return x % m

def insertar(T, m, x, valor):
    j = 0
    h1 = h(convertirLLave(x), m)
    while j < m:
        indice = (h1 + j) % m
        par =[x, valor]
        if  T[indice] == None:
            T[indice] = par
            return indice
        else:
            j = j + 1
    print("No hay lugar")
    return -1

def buscar(T, m, x, valor):
    j = 0
    h1 = h(convertirLLave(x), m)
    while j < m:
        indice = (h1 + j) % m
        if T[indice] != None:
            if T[indice][0] == x:
                return indice
            else:
                j = j + 1
        return -1
    return -1

def main():
    m = 5
    T = formarTabla(m)
    print(T)
    insertar(T, m, "Hola1", "122121")
    insertar(T, m, "Hola2", "122611")
    insertar(T, m, "Hola3", "122231")
    insertar(T, m, "Hola4", "122121")
    insertar(T, m, "Hola5", "122651")
    insertar(T, m, "Hola6", "122321")
    print(T)
    print(buscar(T, m, "Hola5", "122651"))

main()