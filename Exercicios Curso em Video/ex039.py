from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
alistamento = atual + 18 - idade
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    print('Ainda falta {} ano(s) para o alistamento'.format(alistamento - atual))
    print('Seu alistamento será em {}'.format(alistamento))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} ano(s)'.format(atual - alistamento))
    print('Seu alistamento foi em {}'.format(alistamento))
