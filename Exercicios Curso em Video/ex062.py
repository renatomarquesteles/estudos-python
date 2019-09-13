print('Gerador de PA')
print('-=' * 10)
t1 = int(input('Primeiro termo: '))
termo = t1
razao = int(input('Razão: '))
count = 1
total = 0
extra = 10
while extra != 0:
    total += extra
    while count <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    extra = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
