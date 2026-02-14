saldo = 0
extrato = []

def menu():
    print('''\n1 - Entrada
2 - Saída
3 - Ver saldo
4 - Ver histórico
5 - Ver resumo
6 - Sair
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

def resumo():
    if not extrato:
        print("Nenhuma movimentação ainda.")
        print(f"Saldo final: R${saldo:.2f}")
        return

    total_entradas = 0.0
    total_saidas = 0.0

    for linha in extrato:
        valor_str = linha.split()[-1]  # pega "+50.00" ou "-20.00"
        valor = float(valor_str.replace("+", ""))  # float lida com "-" sozinho

        if linha.startswith("Entrada"):
            total_entradas += valor
        elif linha.startswith("Saída"):
            total_saidas += abs(valor)  # deixa positivo para total de saídas

    print("=== RESUMO ===")
    print(f"Operações: {len(extrato)}")
    print(f"Total de entradas: R${total_entradas:.2f}")
    print(f"Total de saídas:   R${total_saidas:.2f}")
    print(f"Saldo final:       R${saldo:.2f}")


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
        resumo()
    elif entrada == 6:
        print('Finalizando programa... ')
        break
    else: 
        print('Número invalido.')
        continue

