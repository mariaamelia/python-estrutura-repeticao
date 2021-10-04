def leiaEntrada(msg):
    ok = False
    entrada = ""
     
    while True:
        entrada = input(msg)
        if entrada != "":
            ok = True
        else:
            print(msg)
        if ok:
            break
    return entrada

def calculaCrescimento(populacaoA, populacaoB,taxaA, taxaB) :
    anos = 0
    while populacaoA < populacaoB:
        populacaoA = populacaoA + (populacaoA * taxaA)
        populacaoB = populacaoB + (populacaoB * taxaB)
        anos = anos + 1
    return anos


okTermina = False
paisA = 0
paisB = 0
taxaA = 0
taxaB = 0

while True:
    msgPaisA = "Informe a população do Primeiro pais:....."
    a = leiaEntrada(msgPaisA)

    try:
        paisA = int(a)
        if(paisA > 0 ):
            msgTxPaisA = "Informe a taxa de crescimento:....."
            b = leiaEntrada(msgTxPaisA)
            taxaA = float(b)
            if taxaA > 0:
                msgPaisB = "Informe a população do Segundo pais:....."
                c = leiaEntrada(msgPaisB)
                paisB = int(c)
                if paisB > 0 :
                    msgTxPaisB = "Informe a taxa de crescimento:....."
                    d = leiaEntrada(msgTxPaisB)
                    taxaB = float(d)
                    if taxaB > 0: 
                        anos = calculaCrescimento(paisA,paisB,taxaA/100, taxaB/100)
                        print ("Serão necessários " + str(anos) + " anos para que a população do pais A ultrapasse ou iguale a população do pais B")
                        e = leiaEntrada("Deseja fazer novos calculos? s->sim/n->nao  ")
                        if e == 'n':
                            okTermina = True
                    else:
                        print("Informe um valor maior que zero")

            else:
                print("Informe um valor maior que zero")

        else:
            print("Informe um valor maior que zero")
    except ValueError:
        print("Informe um numero valido.")

    if okTermina :
        break

