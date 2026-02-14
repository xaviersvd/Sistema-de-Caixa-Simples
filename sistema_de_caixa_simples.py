saldo = 0

def menu():
    print('''\n1 - Adicionar dinheiro (entrada)
2 - Registrar saída (gasto)
3 - Ver saldo
4 - Sair
\n''')

def adicionar_dinheiro():
    global saldo
    while True:
        valor = int(input('Digite um valor: (Para voltar ao menu principal digite 0): '))
        saldo += valor
        if valor == 0:
            break

def registrar_saidia():
    global saldo
    while True:
        valor = int(input('Digite o valor que vai ser retirado do caixa: (Para voltar ao menu principal digite 0): '))
        if saldo < valor:
            print('Saldo insuficiente!')
        saldo -= valor
        if valor == 0:
            break


while True:
    menu()
    entrada = int(input('Digite uma opção: '))
    if entrada == 1:
        adicionar_dinheiro()
    elif entrada == 2:
        registrar_saidia()
    elif entrada== 3:
        print(f'Seu saldo é de: {saldo}')
    elif entrada== 4:
        print('Finalizando programa... ')
        break
    else: 
        print('Número invalido.')
        continue

