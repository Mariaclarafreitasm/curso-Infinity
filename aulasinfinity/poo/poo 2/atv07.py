from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,nome,raça):
        self.nome = nome
        self.raça = raça
    @abstractmethod    
    def comer(self):
        return f"O {self.nome} esta comendo"

class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome, raça)
    def latir(self):
        return f"O cachorro {self.nome} esta latindo"

cachorro1 = Cachorro("duke","caramelo")
# print(cachorro1.comer())
print(cachorro1.latir())