bandera_dijkstra = []
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
 