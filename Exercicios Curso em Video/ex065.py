resp = 'S'
soma = qtd = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
print('Você digitou {} números e a média foi {}'.format(qtd, soma / qtd))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
