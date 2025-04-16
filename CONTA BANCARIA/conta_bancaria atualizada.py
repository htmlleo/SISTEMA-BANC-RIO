class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular  # Usuario
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    def extrato_conta(self):
        print(f"\nExtrato da conta {self.numero} - Titular: {self.titular.nome}")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")


# Banco de dados (simulado com listas)
usuarios = []
contas = []


def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    cpf = input("CPF do usuário: ")

    # Verifica se CPF já existe
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Usuário com esse CPF já cadastrado.")
            return usuario

    novo_usuario = Usuario(nome, cpf)
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return novo_usuario


def criar_conta(usuario):
    numero = len(contas) + 1  # Simples auto incremento
    nova_conta = ContaBancaria(numero, usuario)
    contas.append(nova_conta)
    usuario.adicionar_conta(nova_conta)
    print(f"Conta número {numero} criada com sucesso para {usuario.nome}!")
    return nova_conta


def encontrar_conta_por_cpf():
    cpf = input("Digite o CPF: ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            if usuario.contas:
                return usuario.contas[0]  # Retorna a primeira conta associada
            else:
                print("Usuário não possui conta ainda.")
                return None
    print("Usuário não encontrado.")
    return None


def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cadastrar Usuário")
        print("2 - Criar Conta Bancária")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Ver Extrato")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = cadastrar_usuario()  # Pode reutilizar o retorno
            criar_conta(usuario)
        elif opcao == "3":
            conta = encontrar_conta_por_cpf()
            if conta:
                valor = float(input("Valor do depósito: R$"))
                conta.depositar(valor)
        elif opcao == "4":
            conta = encontrar_conta_por_cpf()
            if conta:
                valor = float(input("Valor do saque: R$"))
                conta.sacar(valor)
        elif opcao == "5":
            conta = encontrar_conta_por_cpf()
            if conta:
                conta.extrato_conta()
        elif opcao == "6":
            print("Saindo... Obrigado por usar o sistema bancário.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
