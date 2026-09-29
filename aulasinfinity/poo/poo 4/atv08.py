class ContaBancaria:
    def __init__(self,saldo,numero_conta):
        self.__saldo = saldo
        self.__numero_conta = numero_conta

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self,deposito):
        return self.__saldo + deposito

    def sacar(self,saque):
        if saque > self.__saldo:
            print('nao pode sacar')
            return self
        else:
            return self.__saldo - saque

    