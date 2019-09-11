peso = float(input('Qual é seu peso(kg)? '))
altura = float(input('Qual é sua altura(m)? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Cuidado! Você está ABAIXO DO PESO')
elif imc < 25:
    print('Você está no PESO IDEAL')
elif imc < 30:
    print('Você está SOBREPESO')
elif imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Cuidado! Você está em OBESIDADE MÓRBIDA!')
