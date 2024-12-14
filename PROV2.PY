total=0
T=0
S=1
A=int(input("digite um numero: "))
B=int(input("digite um numero: "))
total=A+B
M=int(input("quantas vezes voce quer repetir: "))
for i in range(M):
    U=int(input("digite um numero: "))
    
    if T < S:
     total=total*U
     T+=1
    else:
      S< T 
    total=total+U
    S+=1
print(S)
print(T)
print(total)
          