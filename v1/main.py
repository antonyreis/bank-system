menu = """

[d] - Depositar Valor
[s] - Sacar Valor
[e] - Imprimir Extrato
[q] - Sair

"""

saldo = 0
limite_valor = 500
LIMITE_SAQUES = 3
saques_realizados = 0
extrato = []


def depositar():
    global saldo
    valor = float(input("Informe o valor que você deseja depositar: "))

    if valor <= 0:
        return("Valor depositado inválido.")

    saldo += valor
    atualiza_extrato("Depósito", saldo, valor)

    return f"""
            Operação realizada com sucesso!
            Saldo Atualizado: R$ {saldo:.2f}
            """

def sacar():
    global limite_valor
    global LIMITE_SAQUES
    global saldo

    if saldo <= 0:
        return "Não há valor disponível para saque."
    
    if saques_realizados == LIMITE_SAQUES:
        return "Limite de saques excedido, tente novamente outro dia."
     
    valor = float(input("Informe o valor que deseja sacar: "))

    if valor > limite_valor:
        return f"Valor inserido inválido. Seu limite de saque é R$ {limite_valor:.2f}."

    elif valor > saldo:
        return f"Valor indisponível na conta. Saldo disponível: {saldo:.2f}"

    saldo -= valor
    saques_realizados += 1
    atualiza_extrato("Saque", saldo, valor)

    return f"""
            Operação realizada com sucesso!
            Saldo Atualizado: R$ {saldo:.2f}
            """

def atualiza_extrato(op, saldo, valor):
    extrato.append(f"{op} no valor de R$ {valor:.2f}. Saldo final: R$ {saldo:.2f}")

def imprime_extrato():
    print("==== EXTRATO BANCÁRIO ====", end="\n")

    for operacao in extrato:
        print(f"{operacao}")

    return f"\nSaldo: R$ {saldo:.2f}"

def sair():
    return """
        Obrigado por ser nosso cliente hoje!
        Até a próxima!
        """

def main():
    print("Seja bem vindo ao nosso sistema bancário! \n")
    while True:
        print(menu)
        opcao = input("Digite a opção que deseja selecionar: ")

        OPCOES_VALIDAS = {
            "d": depositar,
            "s": sacar,
            "e": imprime_extrato,
            "q": sair
        }

        if opcao.lower() not in OPCOES_VALIDAS.keys():
            print("Opção Inválida! Por favor selecione uma das opções disponíveis.")

        elif opcao.lower() == "q":
            print(OPCOES_VALIDAS[opcao.lower()]())
            break

        else:
            print(OPCOES_VALIDAS[opcao.lower()]())

main()