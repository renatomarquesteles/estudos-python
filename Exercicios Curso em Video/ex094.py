pessoas = []
soma_idade = 0
while True:
    pessoa = {
        "Nome": input('Nome: ').strip(),
        "Sexo": input('Sexo [M/F]: ').strip()
    }
    while pessoa["Sexo"].upper() not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoa["Sexo"] = input('Sexo [M/F]: ').strip()
    pessoa["Idade"] = int(input('Idade: '))
    soma_idade += pessoa["Idade"]
    pessoas.append(pessoa)
    resp = input('Quer continuar? [S/N]: ')
    while resp.lower() not in 'sn':
        print('ERRO! Responda apenas S ou N.')
        resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break
print('-=' * 20, end='-\n')
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma_idade/len(pessoas):5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p["Sexo"] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['Idade'] >= soma_idade/len(pessoas):
        print('     ', end='')
        for k, v in p.items():
            print(f'{k}: {v}; ', end='')
        print()
print('<< ENCERRADO >>')
