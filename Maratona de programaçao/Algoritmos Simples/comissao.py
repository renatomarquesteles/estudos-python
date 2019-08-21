n_vendedor = input("Informe o nome do vendedor: ")
sal_fixo = float(input("Salário fixo do vendedor: "))
vendas = int(input("Quantidade de vendas no mês: "))
salario_total = (vendas*0.2)+sal_fixo
print("O salário final do vendedor "+str(n_vendedor)+" é "+str(salario_total))
