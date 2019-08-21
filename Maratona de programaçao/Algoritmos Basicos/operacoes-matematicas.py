def operacoes():
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite um outro número inteiro: "))
    print("Soma: " + str(n1+n2))
    print("Diferença: " + str(n1-n2))
    print("Produto: " + str(n1*n2))
    if n2 == 0:
        print("Não é possível dividir por zero")
    else:
        print("Divisão: " + str(n1/n2))


operacoes()
