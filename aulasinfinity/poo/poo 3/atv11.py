class Conta:
    def __init__(self,id,saldo):
        self.id  = id
        self.__saldo = saldo
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,deposito):
        self.__saldo = deposito

    # def get_saldo(self):
    #     return self.__saldo
    # def set_saldo(self,deposito):
    #     self.__saldo +=deposito

conta1 = Conta(121,1000)
conta1.saldo = 100
print(conta1.saldo)