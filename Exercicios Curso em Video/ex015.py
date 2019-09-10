dias = int(input('Quantos dias alugados? '))
distancia = float(input('Quantos km rodados? '))
print('O total a pagar é R${:.2f}'.format(60*dias + 0.15*distancia))
