import random as rn
x=input("Ingrese primeros 2 digitos: ")
lista=[]
for j in range(1000):
  t=x
  for i in range(7):
    n=rn.randint(0,9)
    t+=str(n)
  lista.append(t)
print(lista)


for j in range(len(lista)):
  elemento =lista[j]
  #print(elemento)
  valor1=0
  valor2=0
  for i in range(len(elemento)):
    if (i)%2==0:
      value=int(elemento[i])*2
      if value>9:
        value-=9
      valor1+=value
    else:
      valor2+=int(elemento[i])
    total=valor1+valor2
  valor3=total%10
  if (valor3)==0:
    verificador=0
  else:
    verificador=10-valor3
  lista[j]+=str(verificador)
  
print(lista)