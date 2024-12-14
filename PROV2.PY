total = 0
T = 0
A = int(input("digite um numero: "))
B = int(input("digite um numero: "))
total = A + B
M = int(input("quantas vezes voce quer repetir: "))

for i in range(M):
    U = int(input("digite um numero: "))

    if T == 0:  # Verifica se é a primeira iteração
        total = total * U
    else:
        total = total + U
    T += 1  # Incrementa T em todas as iterações

print("Contagem:", T)
print("Total:", total)
