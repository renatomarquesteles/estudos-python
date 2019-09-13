maior_18 = n_homens = menor_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        n_homens += 1
    if sexo == 'F' and idade < 20:
        menor_20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {n_homens} homens cadastrados')
print(f'E temos {menor_20} mulheres com menos de 20 anos')
