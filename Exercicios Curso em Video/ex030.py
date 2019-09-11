num = int(input('\033[35mMe diga um número qualquer: \033[m'))
if num % 2 == 0:
    print('O número \033[1m{}\033[m é \033[4;36mPAR\033[m'.format(num))
else:
    print('O número \033[1m{}\033[m é \033[4;36mÍMPAR\033[m'.format(num))
