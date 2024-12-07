#criar uma lista para armazenar os numeros de forma que nao some ou rescreva os numeros ja armazenados 
numeros=[]
#primeiro vamos pedir ao usuario os numeros   fazemos um  for para nao ter que pedir 20 vezes 
for i in range(20):
 n=int(input('digite um numero maiorou igual a 0 (digite um numero negativo para parar):'))
  # se o usuario digitar um numero menor que zero  sera interompido a função de pedir 
 if n<0:
  break
 # adicionamos os numeros  dados pelo usuario na lista numero 
 numeros.append(n)
 #inicio varios contadores para numero de vezes que cada numero apareceseu 
contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0
# no caso nesse aqui em baixo o exercicio nao deixava claro se vc queria de 0 ate 100  entao eu coloquei a mais para contar  os numeros maiores que 100
contador_maior_que_100 = 0
#começamos  a fazer um for de if para checar cada ves que os numeros aparecem 
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
    #aqui printamos tudo no caso tem um que é desnecessario mas eu coloquei para ver se esta certo o for  acima 
print(numeros)
print(contador_0_25)
print(contador_26_50)
print(contador_51_75)
print(contador_76_100)
