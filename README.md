# Definindo a classe Cliente
class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Email: {self.email}"


# Definindo a classe ContaBancaria
class ContaBancaria:
    def __init__(self, cliente, numero_conta, saldo_inicial=0.0):
        self.cliente = cliente  # A instância de Cliente associada à conta
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Método para realizar um depósito"""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        """Método para realizar um saque"""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")

    def consultar_saldo(self):
        """Método para consultar o saldo"""
        return f"Saldo atual: R${self.saldo:.2f}"

    def __str__(self):
        return f"Conta: {self.numero_conta}, Cliente: {self.cliente.nome}, Saldo: R${self.saldo:.2f}"


# Exemplo de uso
cliente1 = Cliente("João Silva", "123.456.789-00", "joao@email.com")
conta1 = ContaBancaria(cliente1, "001", 1000.00)

print(cliente1)  # Exibindo dados do cliente
print(conta1)    # Exibindo dados da conta

conta1.depositar(500.00)  # Depósito de R$500.00
conta1.sacar(200.00)      # Saque de R$200.00
print(conta1.consultar_saldo())  # Exibindo saldo após as transações

# Criando outro cliente e conta
cliente2 = Cliente("Maria Oliveira", "987.654.321-00", "maria@email.com")
conta2 = ContaBancaria(cliente2, "002")

conta2.depositar(150.00)
print(conta2.consultar_saldo())  # Verificando o saldo de Maria
