#iniciamos os 2 acumuladores um para a mutiplicação e outro para a soma total dos calculos 
ACU=2
total=0
#pedimos ao usuario quantas vezes ele quer repetir  a função
m=int(input("quantas vezes vc quer fazer: "))
for i in range(m):
 # esse for vai repetir o quanto o usuario queira  assim nao vai ficar grande o programa 
 A=int(input("digite um numero:"))
#calcular esse numero  vezes o acumulador 
 c1=(ACU*A)
#ADICIONAMOS  o c1 no acumulador total e +1 no  ACU
 total=total+c1
 ACU= ACU+1

print(ACU)