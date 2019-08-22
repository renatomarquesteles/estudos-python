linha = input().split()
a = linha[0]
b = linha[1]
c = linha[2]
d = linha[3]
varetas = [a, b, c, d]
if a > b + c and a > b + d and a > c + d:
    varetas.remove(a)
if b > a + c and b > a + d and b > c + d:
    varetas.remove(b)
if c > a + b and c > a + d and c > b + d:
    varetas.remove(c)
if d > a + b and d > a + c and d > b + c:
    varetas.remove(d)

if len(varetas) < 3:
    print('N')
else:
    print('S')
