"""
    Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome 
    do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""

def leiaEntrada(msg):
    ok = False
    entrada = ""
     
    while True:
        entrada = str(input(msg))
        if entrada != "":
            ok = True
        else:
            print(msg)
        if ok:
            break
    return entrada

okTermina = False
while True:
    msgNomeUsuario = "Informe o nome:....."
    nomeUsuario = leiaEntrada(msgNomeUsuario)

    senhaUsuario = leiaEntrada("Informe a senha do usuario:")

    if nomeUsuario != senhaUsuario:
        okTermina = True
    else:
        print("\033[0;31mO nome do usario deve ser diferente da senha\033[m")
    if okTermina :
        break