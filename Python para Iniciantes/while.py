# contador = 0
# while contador < 5:
#     print('Ainda nao deu')
#     contador = contador + 1
# print('Agora deu')
#
# while contador < 999:
#     print('Ta dando')
#     contador = contador + 1
#     if contador == 10:
#         break
# print('Deu')

numero = int(input('Digite um numero: '))
fatorial = numero
contador = 1
while (numero-contador) > 1:
    fatorial = fatorial*(numero-contador)
    contador += 1
print('{}! = {}'.format(numero, fatorial))
