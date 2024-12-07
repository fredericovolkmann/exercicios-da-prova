numeros=[]
#primeiro vamos pedir ao usuario os numeros
for i in range(20):
 n=int(input('digite um numero maiorou igual a 0 (digite um numero negativo para parar):'))
 if n<0:
  break
 
 numeros.append(n)
contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0
contador_maior_que_100 = 0
for numero in numeros:
 if 0 <= numero <=25:
  contador_0_25 +=1
 elif 26<= numero <=50:
  contador_26_50 +=1
 elif 51 <= numero <= 75:
  contador_51_75 +=1
 elif 76 <= numero <= 100:
  contador_76_100 +=1
 elif 101 <= numero:
    contador_maior_que_100 +=1
print(numeros)
print(contador_0_25)
print(contador_26_50)
print(contador_51_75)
print(contador_76_100)