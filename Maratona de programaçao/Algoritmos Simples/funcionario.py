nome = input("Nome do funcionário: ")
horas_trab = int(input("Horas trabalhadas: "))
valor_hora = float(input("Valor por hora: "))
renda = horas_trab*valor_hora
print("O funcionário "+str(nome)+" deve receber R$ "+str(renda)+" reais")
print("O funcionário {} deve receber R${:.2f} reais".format(nome, renda))
