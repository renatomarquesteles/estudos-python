from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
computador = randint(0, 10)
chute = int(input('Qual é seu palpite? '))
n_chutes = 1
while chute != computador:
    if chute < computador:
        print('Mais.. Tente novamente.')
    else:
        print('Menos.. Tente novamente.')
    n_chutes += 1
    chute = int(input('Qual é seu palpite? '))
print('PARABÉNS! Acertou após {} tentativa(s).'.format(n_chutes))
