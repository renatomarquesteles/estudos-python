D = int(input())
l1 = input().split()
l2 = input().split()
l3 = input().split()
digito = []
result = ''

braille = [
    '.***..',
    '*.....',
    '*.*...',
    '**....',
    '**.*..',
    '*..*..',
    '***...',
    '****..',
    '*.**..',
    '.**...',
]

for i in range(D):
    digito.append(l1[i] + l2[i] + l3[i])

for x in digito:
    result += str(braille.index(x))

print(result)
