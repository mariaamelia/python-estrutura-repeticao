"""

Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""

def comparaLista(lista, valor):
    achou = False
    for item in lista :
        if str(item) == str(valor).lower() :
            achou = True
            break
    return achou


def leiaEntrada(msg, tipo=1):
    ok = False
    entrada = ""
    numero = 0
    while True:
        entrada = str(input(msg)).upper()
        if entrada != "":
            if tipo == 1:
                if not (len(entrada) < 3) :
                    ok = True
                else:
                    print("Informe um nome pelo menos com 3 digitos.")
            elif tipo == 2:
                try : 
                    numero = int(entrada)
                    if numero <= 150:    
                        ok = True                    
                except ValueError  :
                    print("(-_-) Informe uma idade entre 0 e 150 ")            
            elif tipo == 3 :
                try:
                    salario = float(entrada)
                    if salario > 0 :
                        ok = True
                except ValueError:
                    print("(-_-) Informe um salario maior que zero ")
            elif tipo == 4:
                sexo = str(entrada)
                if len(sexo) == 1  and ( sexo.upper() == "F" or sexo.upper()=="M"):
                    ok = True
                else:
                    print("(-_-) Informe F->Femino ou M-> masculino ")
            elif tipo == 5 :
                estadoCivil = str(entrada)
                arrEstadoCivil = ['c','s','d','v']
                if len(estadoCivil) == 1 and comparaLista( arrEstadoCivil, estadoCivil ) :
                    ok =True
                else:
                    print("(-_-) Informe S->Solteiro, C->Casado, D->Divorciado,V->Viúvo ")

            else:
                ok = True
        else:
            print(msg)
        if ok:
            break
    return entrada

    
okTermina = False
while True:
    msgNomeUsuario = "Informe o seu nome:....."
    nomeUsuario = leiaEntrada(msgNomeUsuario)

    if nomeUsuario !="":
        idadeUsuario = leiaEntrada("Informe a sua idade entre 0 e 150 anos:.....",2)
        if idadeUsuario != "" :
            salario = leiaEntrada("Informe o salario maior que zero:....",3)
            if float(salario) > 0 :
                sexo = leiaEntrada("Informe o sexo. Digite F-> Feminino e M->masculino:......",4)                
                if sexo != "" :
                    estadoCivil = leiaEntrada("Informe S->Solteiro, C->Casado, D->Divorciado,V->Viúvo ",5)
                    okTermina = True
                
    else:
        print("\033[0;31mO nome do usario deve ser diferente da senha\033[m")
    
    if okTermina :
        break