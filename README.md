# ejercicios-recursividad-2
Mi dirección de Github es:https://github.com/claudiaalozano/ejercicios-recursividad-2.git

-1. Búsqueda por dicotomía en una tabla ordenada

En este ejercicio nos pide una busqueda recursiva por dicotomía de una tabla y para realizarlo, he empleado el siguiente código:
```lista = ["gato" , "ángel" , "fiesta" , "senderismo" , "pan" , "bebida"]
indice = 0
palabra = input("Seleccione la palabra que desea buscar en la tabla: ")

def buscar (lista, palabra, indice):
  if palabra == str(lista[indice]):
    print("Se encuentra en la tabla")
  else:
    if indice < (len(tabla)-1):
      indice = indice +1
      buscar(lista, palabra, indice)
```

-2. Palíndromos
En este ejercicio nos pide introducir una cadena y que el programa nos devuelva si se trata de palíndromo o no, y para realizarlo he empleado el siguiente código:

```entrada = input("Introduzca la cadena que desea analizar  comprobar si es un palíndromo: ")
entrada.lstrip()
palindromo(entrada)
def palindromo (algo):
  lista = list(entrada)
def notilde(s)
  remplazar = [("á" , "a"),
           ("é" , "e"),
           ("í" , "i"),
           ("ú" , "u"),
           ("ó" , "o")]
  for entrada in remplazar :
    s = s.raplace(entrada)

revertir_cadena=[]
i= len(entrada)
while i > 0:
  revertir_cadena += entrada[i-1]
  i= i - 1
if revertir_cadena is True:
  print("La cadena de texto que usted ha introducido, es un palindromo")
else:
  print("La cadena de texto que usted ha introducido, no es un palindromo")
```

-3. La bandera de Dijkstra
En este programa nos piden ordenar la bandera con un número de fichas y para realizarlo he empleado el siguiente código:

```bandera_dijkstra = []
fichas = ["V" , "R" , "A" , "A" , "R" , "V" , "R" , "A" , "R" , "V" , "V"]
A = []
V = []
R = []
def ordenar (bandera_dijkstra):
  if len(bandera_dijkstra) > 0:
    color= bandera.pop(0)
    if color == "A":
      A.append(color)
      ordenar(bandera_dijkstra)
    if color == "V":
      V.append(color)
      ordenar(bandera_dijkstra)
    if color == "R":
      R.append(color)
      ordenar(bandera_dijkstra)
  else:
    ordenada = A + V + R
    print ("La bandera ya esta ordenada, " , ordenada)
ordenar(bandera_dijkstra)
```
