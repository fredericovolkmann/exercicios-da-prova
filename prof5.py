def calcular_numero_de_vezes(pen_drive_capacity, arquivos):
    # Ordenar o vetor de arquivos em ordem decrescente
    arquivos.sort(reverse=True)
    
    num_vezes = 0  # Inicializamos o contador de vezes que o pen drive será usado
    
    # Enquanto houver arquivos para copiar
    while len(arquivos) > 0:
        capacidade_atual = pen_drive_capacity  # é a Capacidede inicial do pen drive
        num_vezes += 1  # Iniciar uma nova rodada de uso do pen drive
        
        i = 0
        while i < len(arquivos):
            if arquivos[i] <= capacidade_atual:  # Se o arquivo cabe no pen drive
                capacidade_atual -= arquivos[i]  # diminui o tamanho do arquivo da capacidade
                arquivos[i] = 0  # Marca o arquivo como usado
            i += 1
        
        # Remove os arquivos que já foram  usados (com tamanho 0)
        arquivos = [tamanho for tamanho in arquivos if tamanho > 0]
    
    return num_vezes


# Entrada de dados:
l = int(input('Quantos arquivos? '))  # Número de arquivos
arq = []  # Lista de arquivos

for i in range(l):
    a = int(input(f"Qual tamanho do arquivo {i+1}? "))  # Tamanho de cada arquivo decidido pelo usuario 
    if a <= 1000:  # Verifica se o tamanho é menor ou igual a 1000MB
        arq.append(a)
    else:
        print("Arquivo muito grande! Deve ser no máximo 1000MB.")

# Capacidade do pen drive em MB (1GB)
pen_drive_capacity = 1000

# chama a  função e calcula o número mínimo de vezes que o pen drive será usado
num_vezes = calcular_numero_de_vezes(pen_drive_capacity, arq)

# mostra o resultado
print(f"Será necessário usar o pen drive {num_vezes} vezes.")



