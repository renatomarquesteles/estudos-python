linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

MaiorAB = (a+b+abs(a-b))/2
MaiorABC = (MaiorAB+c+abs(MaiorAB-c))/2
print('{:.0f} eh o maior'.format(MaiorABC))
