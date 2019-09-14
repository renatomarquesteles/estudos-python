jogador = {"nome": input('Nome do jogador: '), "gols": []}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    jogador["gols"].append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador["total"] = sum(jogador["gols"])
print(jogador)
for k, v in jogador.items():
    print(f'{k}: {v}')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
