class Veiculo:
    def __init__(self,cor,modelo):
        self.cor = cor
        self.modelo = modelo
    def mudar_cor(self,nova_cor):
        self.cor = nova_cor
        return f" {self.cor} é a cor do veiculo"

    def novo_modelo(self,novo_modelo):
        self.modelo = novo_modelo
        return f"{self.modelo} é o modelo do veiculo"

class Carro(Veiculo):
    def __init__(self, cor, modelo):
        super().__init__(cor, modelo)

class Bicileta(Veiculo):
    def __init__(self, cor, modelo):
        super().__init__(cor, modelo)

carro1 = Carro("preto","celta")
print(carro1.mudar_cor("vermelho"))
print(carro1.novo_modelo("sedan"))
