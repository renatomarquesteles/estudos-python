valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
ano_fin = int(input('Quantos anos de financiamento?'))
prestacao = valor_casa / (ano_fin * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, ano_fin, prestacao))
if prestacao > salario_comprador * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo ACEITO!')
