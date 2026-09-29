class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def exibir_saldo(self):
        return f"{self.saldo} é o saldo "

class ContaSalario(ContaBancaria):
    def __init__(self, titular, saldo,limite_saque_diario):
        super().__init__(titular, saldo)
        self.limite = limite_saque_diario
    def sacar(self,valor_saque):
        if valor_saque > self.saldo or valor_saque > self.limite:
            return self.saldo
        else:
            self.saldo -= valor_saque
            self.limite-=valor_saque
            return self.saldo

conta1 = ContaSalario("pedro",2000,1000)
conta1.sacar(900)
print(conta1.exibir_saldo())