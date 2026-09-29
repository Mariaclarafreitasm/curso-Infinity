class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos")
    def fazer_aniversario(self):
        self.idade +=1
        print(f"Parabens,{self.nome}! Agora voce tem {self.idade}")


    def alterar_nome(self,novo_nome):
        self.nome = novo_nome

pessoa1 = Pessoa("joao",24)
pessoa1.alterar_nome("Joao Pedro")
print(pessoa1.nome)
        