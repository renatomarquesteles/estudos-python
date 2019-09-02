linha = input().split()
hora_inicio = int(linha[0])
minuto_inicio = int(linha[1])
hora_final = int(linha[2])
minuto_final = int(linha[3])

if hora_inicio > hora_final:
    hora_final = hora_final + 24

inicio = (hora_inicio * 60) + minuto_inicio
fim = (hora_final * 60) + minuto_final

duracao = fim - inicio

if duracao == 0:
    duracao = 24 * 60

horas = duracao // 60
minutos = duracao % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
