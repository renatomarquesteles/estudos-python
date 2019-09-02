linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

pi = 3.14159
tri = (A * C) / 2
circ = pi * C**2
trap = ((A + B) / 2) * C
quad = B ** 2
ret = A * B

print(
    'TRIANGULO: {:.3f}\n'
    'CIRCULO: {:.3f}\n'
    'TRAPEZIO: {:.3f}\n'
    'QUADRADO: {:.3f}\n'
    'RETANGULO: {:.3f}'.format(tri, circ, trap, quad, ret))
