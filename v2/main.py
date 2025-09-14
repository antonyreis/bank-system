menu = """

[d] - Depositar Valor
[s] - Sacar Valor
[e] - Imprimir Extrato
[u] - Cadastrar Usuário
[c] - Criar Nova Conta
[l] - Listagem
[q] - Sair

"""

menu_listas = """
          
O que você deseja listar?
        
[1] - Listar Usuários
[2] - Listar Contas
[3] - Voltar para Menu
    
"""

saldo = 0
limite_valor = 500
saques_realizados = 0

extrato = []
usuarios = []
contas = []

LIMITE_SAQUES = 3

def cria_usuario():
    cpf = input("Digite o CPF do novo usuário: ").replace(".", "").replace("-", "")
    has_usuario = any(cpf == usuario_existente["cpf"] for usuario_existente in usuarios)

    if has_usuario:
        print(f"Não é possível cadastrar outro usuário com mesmo CPF.")
        return ""

    else:
        nome = input("Digite o nome do novo usuário: ")
        data_nascimento = input("Digite a data de nascimento do novo usuário: ")
        endereco = input("Digite o nome do novo usuário:\n(LOGRADOURO - NÚMERO - BAIRRO - CIDADE - ESTADO) \n")
        

        novo_usuario = { 
            "nome": nome, 
            "data_nascimento": data_nascimento, 
            "cpf": cpf, 
            "endereco": endereco 
        }
        usuarios.append(novo_usuario)

        print(f"Usuário {nome.title()} criado com sucesso.")
        return ""

def cria_conta():

    cpf_limpo = input("Digite o CPF do usuário dessa nova conta: ").replace(".","").replace("-","")
    usuario = next(
        (usuario_existente for usuario_existente in usuarios if usuario_existente["cpf"] == cpf_limpo),
        None
    )

    if not usuario:
        print(f"Nenhum usuário encontrado com o CPF inserido.")
        return ""

    else:
        conta = {
            "agencia": "0001", 
            "numero_conta": len(contas) + 1, 
            "usuario": usuario
        }

        contas.append(conta)
        print(f"Conta {conta['agencia']}-{conta['numero_conta']} criada para usuário {usuario['nome']} com sucesso.")
        return ""

def lista() -> None:

    def lista_usuario():
        print(f"==== LISTA DE USUÁRIOS ====")
        if len(usuarios) > 0:
            for index, usuario in enumerate(usuarios, start=1):
                print(f"{index}. Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Data de Nascimento: {usuario['data_nascimento']}, Endereço: {usuario['endereco']}\n")
            return ""
        
        else:
            return f"Nenhuma usuário cadastrado."
        
    def lista_conta():
        print(f"==== LISTA DE CONTAS ====")
        if len(contas) > 0:
            for index, conta in enumerate(contas, start=1):
                print(f"{index}. Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}\n")
            return ""
        else:
            return f"Nenhuma conta cadastrada."
        
    print(menu_listas)
    opcao = input("Digite a opção que você deseja: ")
    OPCOES_VALIDAS = {
        '1': lista_usuario,
        '2': lista_conta,
        '3': "VOLTAR"
    }
    if opcao not in OPCOES_VALIDAS:
        return "Opção de listagem inválida, voltando para menu principal.\n"
    
    elif opcao == '3':
        return "Voltando para menu principal...\n"

    else: 
        return OPCOES_VALIDAS[opcao]() 
    
def depositar(saldo, valor, /):
    if valor <= 0:
            return("Valor depositado inválido.")
    
    saldo += valor
    atualiza_extrato(saldo, valor, op="Depósito")

    return saldo, f"""
            Operação realizada com sucesso!
            Saldo Atualizado: R$ {saldo:.2f}
            """

def sacar(*, saldo=0.0, valor=0.0):
    global limite_valor, saques_realizados, LIMITE_SAQUES

    if saldo <= 0:
        return saldo, "Não há valor disponível para saque."
    
    if saques_realizados == LIMITE_SAQUES:
        return saldo, "Limite de saques excedido, tente novamente outro dia."

    if valor > limite_valor:
        return saldo, f"Valor inserido inválido. Seu limite de saque é R$ {limite_valor:.2f}."

    elif valor > saldo:
        return saldo, f"Valor indisponível na conta. Saldo disponível: {saldo:.2f}"

    saldo -= valor
    saques_realizados += 1
    atualiza_extrato(saldo, valor, op="Saque")

    return saldo, f"""
            Operação realizada com sucesso!
            Saldo Atualizado: R$ {saldo:.2f}
            """

def atualiza_extrato(saldo, valor, /, op="Transação"):
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
        global saldo
        print(menu)
        opcao = input("Digite a opção que deseja selecionar: ")

        OPCOES_VALIDAS = {
            "d": depositar,
            "s": sacar,
            "e": imprime_extrato,
            "u": cria_usuario,
            "c": cria_conta,
            "l": lista,
            "q": sair
        }

        if opcao.lower() not in OPCOES_VALIDAS.keys():
            print("Opção Inválida! Por favor selecione uma das opções disponíveis.")
            continue

        if opcao.lower() == "q":
            print(OPCOES_VALIDAS[opcao.lower()]())
            break

        elif opcao.lower() == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, msg = OPCOES_VALIDAS[opcao.lower()](saldo=saldo, valor=valor)
            print(msg)
            continue
        
        elif opcao.lower() == "d":
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo, msg = OPCOES_VALIDAS[opcao.lower()](saldo, valor)
            print(msg)
            continue

        print(OPCOES_VALIDAS[opcao.lower()]())

main()