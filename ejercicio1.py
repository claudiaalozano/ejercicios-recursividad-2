lista = ["gato" , "ángel" , "fiesta" , "senderismo" , "pan" , "bebida"]
indice = 0
palabra = input("Seleccione la palabra que desea buscar en la tabla: ")

def buscar (lista, palabra, indice):
  if palabra == str(lista[indice]):
    print("Se encuentra en la tabla")
  else:
    if indice < (len(tabla)-1):
      indice = indice +1
      buscar(lista, palabra, indice)