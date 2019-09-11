print('{:=^40}'.format(' LOJAS TELES '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao not in [1, 2, 3, 4]:
    print('Opção inválida. Tente novamente!')
else:
    if opcao == 1:
        total = preco * 0.9
    elif opcao == 2:
        total = preco * 0.95
    elif opcao == 3:
        total = preco
        parcela = preco/2
        print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    else:
        total = preco * 1.2
        n_parcelas = int(input('Quantas parcelas? '))
        parcela = total/n_parcelas
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(n_parcelas, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
