cliente = input("Informe o nome do cliente: ")
compra = float(input("Valor total da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
v_parcela = compra / parcelas
print("O cliente " + cliente + " comprou " + str(round(compra, 2)) + " em " + str(parcelas) + " parcelas de " + str(
    round(v_parcela, 2)))
