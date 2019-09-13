n = int(input('Digite um número: '))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        count += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, count))
if count == 2:
    print('e por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')
