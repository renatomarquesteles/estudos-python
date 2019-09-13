soma_idade = 0
homem_mais_velho_idade = 0
homem_mais_velho_nome = ''
mulheres_menor_20 = 0
for p in range(1, 5):
    print('{:-^40}'.format(' {}ª PESSOA '.format(p)))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade
    if sexo in 'Mm':
        if p == 1:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome
        elif idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome
    else:
        if idade < 20:
            mulheres_menor_20 += 1
print('A média de idade do grupo é de {} anos'.format(soma_idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_mais_velho_idade, homem_mais_velho_nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres_menor_20))
