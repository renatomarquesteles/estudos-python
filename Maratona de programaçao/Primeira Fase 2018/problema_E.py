msg = input()
crib = input()
errado = 0
for i in range(len(msg)-len(crib)+1):

    for j in range(len(crib)):
        if crib[j] == msg[i:(len(crib) + i)][j]:
            errado += 1
            break

res = (len(msg)-len(crib)+1) - errado
print(res)
