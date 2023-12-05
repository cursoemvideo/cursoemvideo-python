número = int(input('\033[35mMe diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('\033[37mO número {} é \033[34mPAR'.format(número))
else:
    print('\033[37mO número {} é \033[34mÍMPAR'.format(número))
