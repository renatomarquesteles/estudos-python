p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
media = (p1+p2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(p1, p2, media))
if media >= 7:
    print('O aluno está APROVADO')
elif 4 <= media < 7:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')
