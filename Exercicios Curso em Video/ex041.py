from datetime import date
nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
