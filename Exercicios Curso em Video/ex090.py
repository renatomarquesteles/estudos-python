aluno = {}
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['média'] >= 6:
    aluno['situação'] = 'Aprovado'
elif 4 <= aluno['média'] < 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-' * 50)
for k, v in aluno.items():
    print(f'{k.capitalize()}: {v}')
