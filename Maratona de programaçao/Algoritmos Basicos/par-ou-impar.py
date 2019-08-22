def par_ou_impar():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print("O número {} é ímpar".format(numero))


par_ou_impar()
