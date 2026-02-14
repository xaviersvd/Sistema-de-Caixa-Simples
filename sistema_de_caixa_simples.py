saldo = 0

def menu():
    print('''\n1 - Adicionar dinheiro
2 - Ver saldo
3 - Sair
\n''')

def adicionar_dinheiro():
    global saldo
    while True:
        valor = int(input('Digite um valor: (Para voltar ao menu principal digite 0): '))
        saldo += valor
        if valor == 0:
            break
while True:
    menu()
    entrada = int(input('Digite uma opção: '))
    if entrada == 1:
        adicionar_dinheiro()
    elif entrada == 2:
        print(f'O saldo da conta é R${saldo}')
    elif entrada== 3:
        print('Finalizando programa... ')
        break
    else: 
        print('Número invalido.')
        break
