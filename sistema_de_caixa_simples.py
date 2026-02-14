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
        valor = float(input('Digite um valor (0 para voltar): '))
        if valor == 0:
            break
        if valor < 0:
            print("Digite um valor positivo.")
            continue
        saldo += valor

def registrar_saidia():
    global saldo
    while True:
        valor = float(input('Digite o valor da saída (0 para voltar): '))
        if valor == 0:
            break
        if valor < 0:
            print("Digite um valor positivo.")
            continue
        if valor > saldo:
            print('Saldo insuficiente!')
            continue
        saldo -= valor

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

