
def recorrerLetra(cadena, lugares):
  cadenaLista = list(cadena)
  aux = cadenaLista[lugares - 1]
  cadenaLista[lugares - 1] = cadenaLista[lugares - 2]
  cadenaLista[lugares - 2] = aux
  cadenaRecorrida = ""
  for ele in cadenaLista:
    cadenaRecorrida += ele
  return cadenaRecorrida
