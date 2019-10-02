n = int(input())
palavras = []
for i in range(n):
    palavras.append(input())

for s in palavras:
    pares = ''
    impares = ''
    for i in range(len(s)):
        if i % 2 == 0:
            pares += s[i]
        else:
            impares += s[i]
    print(f'{pares} {impares}')
