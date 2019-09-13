n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''\n{:=^30}
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números

[ 9 ] Sair do programa'''.format(' MENU '))
opcao = 0
while opcao != 9:
    opcao = int(input('>>>>> Escolha uma opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('{} * {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 != n2:
            print('O maior número entre {} e {} é: {}'.format(n1, n2, n1 if n1 > n2 else n2))
        else:
            print('Os números inseridos são iguais.')
    elif opcao == 4:
        print('Insira novos valores.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 9:
        print('Fim do programa.')
    else:
        print('Opção inválida.')
