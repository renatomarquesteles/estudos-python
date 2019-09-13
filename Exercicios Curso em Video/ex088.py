from random import randint
print(f'{" MEGA SENA ":=^40}')
n = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
for i in range(0, n):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
