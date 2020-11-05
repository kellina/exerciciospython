# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# Atributos: número da conta, nome do correntista e saldo. 
# Métodos: alterarNome, depósito e saque; 
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__ (self, conta, nome, saldo = 0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alteraNome(self, nome):
        self.nome = nome
    
    def deposito(self, deposito):
        self.saldo += deposito

    def saque (self, saque):
        if self.saldo < saque:
            raise ValueError("Saldo insuficiente!")
        self.saldo -= saque

conta1 = ContaCorrente(123, "João")
try:
    conta1.saque(50)
except ValueError as e:
    print(e)

print("A", conta1.conta, "do(a)", conta1.nome, "tem saldo:", conta1.saldo)
conta1.deposito(100)
print("A", conta1.conta, "do(a)", conta1.nome, "tem saldo de:", conta1.saldo)
conta1.saque(50)
print("A", conta1.conta, "do(a)", conta1.nome, "tem saldo de:", conta1.saldo)