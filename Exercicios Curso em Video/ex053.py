frase = input('Digite uma frase: ').strip().upper()
junto = ''.join(frase.split())
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')
