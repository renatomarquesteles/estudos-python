n = int(input('Digite um número: '))
print('Calculando {}! = '.format(n), end='')
fatorial = 1
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fatorial *= n
    n -= 1
print(fatorial)
