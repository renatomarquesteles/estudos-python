from random import randint
from time import sleep
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
if jogador not in range(3):
    print('Opção inválida. Tente novamente!')
else:
    print('JO ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=' * 20)
    print('Computador jogou', opcoes[computador])
    print('Você jogou', opcoes[jogador])
    print('-=' * 20)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU!')
    elif computador == 1:
        if jogador == 0:
            print('VOCÊ PERDEU!')
        elif jogador == 1:
            print('EMPATE')
        else:
            print('VOCÊ VENCEU!')
    else:
        if jogador == 0:
            print('VOCÊ VENCEU!')
        elif jogador == 1:
            print('VOCÊ PERDEU!')
        else:
            print('EMPATE')