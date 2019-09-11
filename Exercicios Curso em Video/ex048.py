soma = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        count += 1
print('A soma de todos os {} valores solicitados é {}'.format(count, soma))
