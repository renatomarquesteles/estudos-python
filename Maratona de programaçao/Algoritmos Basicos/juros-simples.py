def divida_juros_simples():
    valor = float(input("Digite o valor da divida: "))
    juros = float(input("Digite o valor do juros por dia: "))
    dias_atraso = int(input("Dias de atraso: "))
    valor_total = valor + (valor * (juros / 100) * dias_atraso)
    print("O valor total a pagar é: " + str(valor_total))


divida_juros_simples()
