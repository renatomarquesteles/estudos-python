linha = input().split()
a = int(linha[0])
b = int(linha[1])

q = a // abs(b)
r = a % abs(b)
if a > 0 > b or (a < 0 and b < 0):
    q = q * (-1)
print(q, r)
