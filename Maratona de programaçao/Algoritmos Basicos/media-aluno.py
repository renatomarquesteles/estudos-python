def media_aluno():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1 + n2) / 2
    if media >= 7:
        print("Aluno aprovado")
    elif 4 <= media < 7:
        print("Aluno de exame final")
    else:
        print("Aluno reprovado")
    print("Nota final do aluno: " + str(round(media, 2)))


media_aluno()
