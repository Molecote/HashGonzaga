import hashlib
import random
import string

#Esta função cria várias strings aleatória com um tamanho máximo de 4, igual ao tamanho da senha,
#pra então gerar o hash dessa string e verificar se esse hash está no arquivo com os usuários
def quebrar_hash():
    N = 4
    while True:
        senha = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                usuario, senha_armazenada = linha.strip().split(",")
                if senha_armazenada == senha_hash:
                    print("A senha de", usuario, "é: ", senha)
                    with open("senhas.txt", "a") as crack:
                        crack.write(f"{usuario},{senha}\n")


quebrar_hash()
