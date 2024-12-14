def inserir_pessoa(arquivo):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    with open(arquivo, 'a') as f:
        f.write(f"{nome}\n{telefone}\n{email}\n")

def listar_pessoas(arquivo):
    try:
        with open(arquivo, 'r') as f:
            pessoas = f.readlines()
            if pessoas:
                print("Pessoas cadastradas:")
                for i in range(0, len(pessoas), 3):
                    nome = pessoas[i].strip()
                    telefone = pessoas[i+1].strip()
                    email = pessoas[i+2].strip()
                    print(f"Nome: {nome}\nTelefone: {telefone}\nEmail: {email}\n")
            else:
                print("Não há pessoas cadastradas.")
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")

arquivo = "cadastro.txt"

inserir_pessoa(arquivo)

listar_pessoas(arquivo)
