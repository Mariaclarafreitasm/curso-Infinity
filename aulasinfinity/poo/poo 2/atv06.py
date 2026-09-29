class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def ligar(self):
        return 'ligando o motor'

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano,portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    def bater_porta(self):
        return "porta batida"

carro1 = Carro("FORD","sedan",2020,4)
veiculo = Veiculo("alguma","talvez",1900)
print(carro1.bater_porta())

