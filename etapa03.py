import hashlib
#Função que tem como objetivo criar um hash MD5 do hash MD5 da senha criada pelo usuário,
# assim impedindo o código da etapa 2, que somente cria strings de até 4 digitos/letras.
def protect_hash():
    with open("usuarios.txt","r") as protegendo:
        for i in range(0,4):
            for linha in protegendo:
                usuario, senha_armazenada = linha.strip().split(",")
                with open('usuarios.txt', "a") as protegendo:
                    hash_protect = hashlib.md5(senha_armazenada.encode()).hexdigest()
                    protegendo.write(f'\n{usuario}, {hash_protect}')



protect_hash()