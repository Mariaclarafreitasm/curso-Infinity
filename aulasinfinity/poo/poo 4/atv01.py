class Cachorro:
    def __init__(self,raca,nome,idade,pelo):
        self.raca = raca
        self.nome = nome
        self.idade = idade
        self.pelo = pelo
        self.dormindo = False
    def latir(self):
        print(f"o cachorro {self.nome} esta latindo au au au")
    def dormir(self):
        if self.dormindo == False:
            self.dormindo = True
            print(f"o cachorro {self.nome} esta dormindo")
        else:
            self.dormindo = False
            print(f"o cachorro {self.nome} esta acordado")
cachorro1 = Cachorro("yorkshire","pacoca",5,"marrom")
cachorro2 = Cachorro("yorkshire","mel",5,"marrom")
print(cachorro1.dormindo)
cachorro1.dormir()
print(cachorro1.dormindo)

print(cachorro2.nome)

cachorro1.latir()