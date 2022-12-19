import random 
pares = [2,4,6,8]
impares = [1,3,7,9]

def embaralha():
  global x,y
  x = random.sample(pares,4)
  y = random.sample(impares,4)
  return x, y
  
def defineValores():
  while (x[0]+y[1]+x[2] != 15 or y[0]+5+y[3] != 15 or x[1]+y[2]+x[3] != 15 or x[0]+y[0]+x[1] != 15 or y[1]+y[2]+5 != 15):
      embaralha()
  linha1 = [x[0],y[0],x[1]]
  linha2 = [y[1],  5, y[2]]
  linha3 = [x[2],y[3],x[3]]
  print(linha1)
  print(linha2) 
  print(linha3)
  
embaralha()
defineValores()