def exibir_menu():
    opcoes = """
    ================ MENU ================
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [N] Nova conta
    [L] Listar contas
    [U] Novo usuário
    [Q] Sair
    => """
    valor = input("Escolha uma opção:").upper()
    return valor

def depositar(saldo, valor, historico, /):
    if valor > 0:
        saldo += valor
        historico += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Sucesso Depósito realizado! ===")
    else:
        print("\n Erro Valor inválido.")
    return saldo, historico

def sacar(*, saldo, valor, historico, limite, saques_realizados, max_saques):
    if valor > saldo:
        print("\nSaldo insuficiente.")
    elif valor > limite:
        print("\nFalha ao aceder o limite.")
    elif saques_realizados >= max_saques:
        print("\n Falha! Limite de saques atingido")
    elif valor > 0:
        saldo -= valor
        historico += f"Saque:\t\tR$ {valor:.2f}\n"
        saques_realizados += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\nFalha! Valor inválido.")
    return saldo, historico

def mostrar_extrato(saldo, /, *, historico):
    print("\n================ EXTRATO ================")
    print(historico if historico else "Não foram realizadas movimentações.")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(lista_usuarios):
    cpf = input("CPF (somente números): ")
    if localizar_usuario(cpf, lista_usuarios):
        print("\nUsuário já cadastrado!")
        return
    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")
    lista_usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("=== Usuário criado com sucesso! ===")

def localizar_usuario(cpf, lista_usuarios):
    return next((u for u in lista_usuarios if u["cpf"] == cpf), None)

def criar_conta(agencia, numero, lista_usuarios):
    cpf = input("CPF do usuário: ")
    usuario = localizar_usuario(cpf, lista_usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero": numero, "usuario": usuario}
    print("\nUsuário não encontrado!")

def listar_contas(lista_contas):
    for conta in lista_contas:
        info = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(info)

def main():
    MAX_SAQUES = 3
    AGENCIA_PADRAO = "0001"
    saldo = 0
    limite = 500
    historico = ""
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "D":
            valor = float(input("Valor do depósito: "))
            saldo, historico = depositar(saldo, valor, historico)

        elif opcao == "S":
            valor = float(input("Valor do saque: "))
            saldo, historico = sacar(
                saldo=saldo, valor=valor, historico=historico,
                limite=limite, saques_realizados=saques_realizados,
                max_saques=MAX_SAQUES
            )

        elif opcao == "E":
            mostrar_extrato(saldo, historico=historico)

        elif opcao == "U":
            cadastrar_usuario(usuarios)

        elif opcao == "N":
            numero = len(contas) + 1
            conta = criar_conta(AGENCIA_PADRAO, numero, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "L":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Operação inválida. Tente novamente.")

main()