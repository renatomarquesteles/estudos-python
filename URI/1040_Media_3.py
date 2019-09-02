linha = input().split()
n1 = float(linha[0])
n2 = float(linha[1])
n3 = float(linha[2])
n4 = float(linha[3])

media = (n1*2 + n2*3 + n3*4 + n4)/10

print('Media: %.1f' % media)

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: %.1f' % exame)
    mediaFinal = (media+exame)/2
    if mediaFinal >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print('Media final: %.1f' % mediaFinal)
