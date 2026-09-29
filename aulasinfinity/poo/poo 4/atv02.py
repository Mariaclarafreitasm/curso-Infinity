class Cachorro:
    def __init__(self,nome,idade,raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça
    def latir(self):
        print(f"{self.nome} fala - au au!")
meu_cachorro = Cachorro("duke",2,"caramelo")  
meu_cachorro.latir()    
