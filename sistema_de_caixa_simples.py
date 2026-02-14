saldo = 0
extrato = []

def menu():
    print('''\n1 - Entrada
2 - Saída
3 - Ver saldo
4 - Ver histórico
5 - Ver resumo
6 - Sair
7 - Limpar histórico
\n''')

def salvar_dados():
    with open("extrato.txt", "w", encoding="utf-8") as arq:
        for linha in extrato:
            arq.write(linha + "\n")

def carregar_dados():
    global saldo, extrato
    try:
        with open("extrato.txt", "r", encoding="utf-8") as arq:
            extrato = [linha.strip() for linha in arq if linha.strip()]

        saldo = 0.0
        for linha in extrato:
            valor_str = linha.split()[-1]              
            valor = float(valor_str.replace("+", ""))  
            if linha.startswith("Entrada"):
                saldo += valor
            elif linha.startswith("Saída"):
                saldo += valor 
    except FileNotFoundError:
        extrato = []
        saldo = 0.0


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
        salvar_dados()

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
        salvar_dados()

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
        valor_str = linha.split()[-1]
        valor = float(valor_str.replace("+", "")) 

        if linha.startswith("Entrada"):
            total_entradas += valor
        elif linha.startswith("Saída"):
            total_saidas += abs(valor)  

    print("=== RESUMO ===")
    print(f"Operações: {len(extrato)}")
    print(f"Total de entradas: R${total_entradas:.2f}")
    print(f"Total de saídas:   R${total_saidas:.2f}")
    print(f"Saldo final:       R${saldo:.2f}")

def limpar_historico():
    global extrato, saldo

    if not extrato:
        print("Não tem transações para limpar.")
        return
    
    confirmacao = input('Tem certeza que deseja limpar o historico? [S/N]: ').upper()

    if confirmacao == 'S':
        extrato = []
        saldo = 0.0
        salvar_dados()
    elif confirmacao == 'N':
        print('Operação cancelada.')
    else:
        print('Opção inválida')


carregar_dados()

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
    elif entrada == 7:
        limpar_historico()
    else: 
        print('Número invalido.')
        continue

