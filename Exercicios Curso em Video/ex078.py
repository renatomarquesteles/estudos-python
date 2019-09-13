lista_num = []
maior = 0
menor = 0
for c in range(0, 5):
    lista_num.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = lista_num[c]
    else:
        if lista_num[c] > maior:
            maior = lista_num[c]
        if lista_num[c] < menor:
            menor = lista_num[c]
print(f'Você digitou os valores {lista_num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_num):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_num):
    if v == menor:
        print(f'{i}... ', end='')
print()
