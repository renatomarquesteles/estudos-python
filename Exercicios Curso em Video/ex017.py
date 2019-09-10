from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format((ca ** 2 + co ** 2) ** (1/2)))
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))
