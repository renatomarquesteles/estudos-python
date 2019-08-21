d_percorrida = float(input("Informe a distância percorrida(km): "))
t_combustivel = float(input("Quantidade de combustível(L): "))
c_medio = d_percorrida / t_combustivel
print("O consumo médio de combustível é: " + str(round(c_medio, 2)) + " km/L")
