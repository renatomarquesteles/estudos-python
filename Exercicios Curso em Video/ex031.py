distancia = float(input('Qual é a distância da sua viagem? '))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
