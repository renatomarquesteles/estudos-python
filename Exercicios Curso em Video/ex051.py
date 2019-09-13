print('=' * 40)
print('{:^40}'.format(' 10 TERMOS DE UMA PA '))
print('=' * 40)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for i in range(termo, termo+razao*10, razao):
    print(i, end=' → ')
print('ACABOU!')
