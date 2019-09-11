salario = float(input('Qual é o salário do funcionário? R$'))
novo_salario = salario * 1.1 if salario > 1250 else salario * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo_salario))
