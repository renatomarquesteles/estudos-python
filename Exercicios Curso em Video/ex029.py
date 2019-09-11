velocidade = float(input('\033[1;33mQual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = int((velocidade - 80) * 7)
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('\033[32mTenha um bom dia! Dirija com segurança!')
