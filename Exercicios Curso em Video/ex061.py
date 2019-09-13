print('Gerador de PA')
print('-=' * 10)
t1 = int(input('Primeiro termo: '))
termo = t1
razao = int(input('Razão: '))
count = 1
while count <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    count += 1
print('ACABOU')
