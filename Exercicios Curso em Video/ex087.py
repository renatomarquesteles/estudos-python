matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_col_3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
maior_col_2 = matriz[2][0]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_col_3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_col_2:
                maior_col_2 = matriz[l][c]
    print()
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_col_3}')
print(f'O maior valor da segunda linha é {maior_col_2}')
