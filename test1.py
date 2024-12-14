Y = input("digite uma palavra em letra maiuscula:")
x = list(Y)

A = 0
E = 0
I = 0
O = 0
U = 0

for letra in x:
    if letra == 'A':
        A += 1
    elif letra == 'E':
        E += 1
    elif letra == 'I':
        I += 1
    elif letra == 'O':
        O += 1
    elif letra == 'U':
        U += 1

print("A:", A)
print("E:", E)
print("E:", E)
print("O:", O)
print("U:", U)
