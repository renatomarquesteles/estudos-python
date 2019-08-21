def parabens():
    print('Parabéns para você\nNessa data querida\nMuitas felicidades\nMuitos anos de vida\n')


parabens()


def tem_letra_u():
    frase = input('Digite uma frase: ')
    if 'u' in frase:
        print('Você utilizou a letra u')
    else:
        print('Você não utilizou a letra u')


tem_letra_u()


def soma_quadrados(a, b):
    soma_q = a**2 + b**2
    return soma_q


print(soma_quadrados(3, 4))

