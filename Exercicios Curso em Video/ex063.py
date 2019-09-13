print('Sequência de Fibonacci')
n_termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('1', end='')
count = 3
while count <= n_termos:
    t3 = t1 + t2
    print('', t3, end='')
    t1 = t2
    t2 = t3
    count += 1
print(' FIM')
