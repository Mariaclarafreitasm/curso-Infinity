class Vendedor:
    def __init__(self,nome):
        self.nome = nome

class Loja:
    def __init__(self,nome_loja):
        self.nome_loja = nome_loja
        self.vendedores = []

    def contratar(self,vendedor):
        self.vendedores.append(vendedor)
        # print(f"Vendedor {self.nome} foi adicionado")

    def listar_vendedores(self):
        print(f"Vendedores da loja {self.nome_loja}")
        for vendedor in self.vendedores:
            print(f"-> {vendedor.nome}")

maria = Vendedor("maria")
luis = Vendedor("luis")

loja1 = Loja("Bell salvador")
loja1.contratar(maria)
loja1.contratar(luis)
loja1.listar_vendedores()

print(f"{maria.nome}")