s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
