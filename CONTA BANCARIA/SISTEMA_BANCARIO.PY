class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []  # Para armazenar os extratos das transações

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
        print(f"\nExtrato de {self.titular}:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

# Exemplo de uso do sistema bancário
def main():
    nome_cliente = input("Digite o nome do cliente: ")
    conta = ContaBancaria(nome_cliente)

    while True:
        print("\n--- Menu de Operações ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("4 - Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Digite o valor para depósito: R$"))
            conta.depositar(valor)
        elif escolha == "2":
            valor = float(input("Digite o valor para saque: R$"))
            conta.sacar(valor)
        elif escolha == "3":
            conta.extrato_conta()
        elif escolha == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
