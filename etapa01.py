import hashlib
import etapa02
import etapa03

def cadastrar_usuario():
    nome = input("Digite o nome do usuário (até 20 caracteres): ")
    senha = input("Digite a senha do usuário (4 caracteres): ")

    # Verifica se o nome e a senha possuem o tamanho correto
    if len(nome) <= 20 and len(senha) == 4:
        # Realiza o hash da senha utilizando o algoritmo MD5
        senha_hash = hashlib.md5(senha.encode()).hexdigest()

        # Abre o arquivo no modo de escrita (append) e adiciona os dados do usuário
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{nome},{senha_hash}\n")

        print("Usuário cadastrado com sucesso!")
    else:
        print("Nome ou senha inválidos.")

#Função para autenticar o usuário
def autenticar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    senha_hash = hashlib.md5(senha.encode()).hexdigest()

    # Abre o arquivo no modo de leitura e verifica se o usuário e a senha estão cadastrados
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            usuario, senha_armazenada = linha.strip().split(",")
            if usuario == nome and senha_armazenada == senha_hash:
                print("Usuário autenticado com sucesso!")
                return

    print("Usuário ou senha incorretos.")


# Menu principal
while True:
    print("--- Sistema de Cadastro e Autenticação ---")
    print("1. Cadastrar usuário")
    print("2. Autenticar usuário")
    print("3. ")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        autenticar_usuario()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")
