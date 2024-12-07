# Solicita a string ao usuário
entrada = input("Digite uma string: ")

# isso Converte a string em uma lista de caracteres
vetor = list(entrada)

# Inicializa um vetor vazio para armazenar o reverso
reverso = []

# Preenche o vetor reverso com os caracteres em ordem invertida
for i in range(len(vetor) - 1, -1, -1):
    reverso.append(vetor[i])
# o len(vector) retorna o tamanho da lista   como os indices começam em 0 -1 serve para mostra o verdadeira possisao final EX
# ( em uma string com 5 caracteres o -1 vai fazer o seguinte 5-1=4 por que começa de 0 o indice entao a ultima posição seria 4)
# o segundo -1  indica a posição de parada ja que queremos ir até 0 colocamos -1 ja que o comando para antes do numero colocado)
# e o 3 -1 indica o passo. em cada interação vai se diminuindo 1  até chegar em 0
# Converte o vetor reverso de volta para uma string e exibe
# o i se refere a um elemento especifico da lista vetor.
# se vector for uma lista com['a','b','c','d','e'] e o valor de i for,por exemplo,4,então o vector[4] vai retornar 'e'.
# o append() adiciona o elemento vetor[i]ao final da lista reverso.
#assim cada iteração do laço o caractere na posição i do vetor sera adicionado a lista reverso,uma de cada vez,assim formando a string invertida
print("String ao contrário:", ''.join(reverso))
# o join serve para juntar pois a  lista reverso possui caracteres individuais e o join serve para juntalos em uma unica string de maneira eficiente
#'' é uma string fazia mas aqui ela serve como um separador(o que vai ser colocado entre os elementos da  lista quando forem unidos)

