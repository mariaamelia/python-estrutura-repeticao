"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário 
informe um valor válido.

"""

def leiaEntrada(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            if valor >=0 and valor <= 10 :
                ok = True
            else:
                print("\033[0;31mInforma um valor entre 0 e 10\033[m")
        else:
            print("\033[0;31mErro! Digite uma nota 0 a 10 :....\033[m" )
        if ok:
            break
    return valor

n = leiaEntrada("\nDigite uma nota entre 0 e 10 :....")

print(f'Você digitou o numero .....\033[1;107m  \033[1;32m{n}\033[m')
