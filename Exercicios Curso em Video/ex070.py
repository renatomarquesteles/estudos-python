total = maior_mil = menor = count = 0
barato = ''
while True:
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$'))
    count += 1
    total += preco
    if preco > 1000:
        maior_mil += 1
    if count == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print(f'\nO total da compra foi R${total:.2f}')
print(f'Temos {maior_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
