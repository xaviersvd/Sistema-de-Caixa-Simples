saldo = 0
extrato = []

def menu():
    print('''\n1 - Entrada
2 - Saída
3 - Ver saldo
4 - Ver histórico
5 - Sair

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
        extrato.append(f"Entrada: +{valor:.2f}")

def registrar_saida():
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
        extrato.append(f"Saída: -{valor:.2f}")

def movimentacao():
    if not extrato:
        print("Nenhuma movimentação ainda.")
        return
    for operacao in extrato:
        print(operacao)


while True:
    menu()
    entrada = int(input('Digite uma opção: '))
    if entrada == 1:
        adicionar_dinheiro()
    elif entrada == 2:
        registrar_saida()
    elif entrada == 3:
        print(f'Seu saldo é de: R${saldo:.2f}')
    elif entrada == 4:
        movimentacao()
    elif entrada == 5:
        print('Finalizando programa... ')
        break
    else: 
        print('Número invalido.')
        continue

