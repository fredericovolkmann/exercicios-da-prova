Y=input("digite uma palavra em letra maiuscula:")
lista = [Y]

x = [list(palavra) for palavra in lista]

for i in range(len(x)-1,-1,-1):
 
 A=0
 E=0
 I=0
 O=0
 U=0
 if i==A:
    A+=1
 elif i==E:
    E+=1
 elif i==I:
    I+=1
 elif i==O:
    O+=1
 elif i==U:
    U+=1
 
print(A)
print(E)
print(I)
print(O)
print(U)
 