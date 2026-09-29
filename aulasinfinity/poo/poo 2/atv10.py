class Pedido:
    def __init__(self,nome_produto,preço):
        self.nome = nome_produto
        self.preço = preço

class PedidoEletronico(Pedido):
    def __init__(self, nome_produto, preço,serial_number):
        super().__init__(nome_produto, preço)
        self.serial = serial_number

class PedidoRoupa(Pedido):
    def __init__(self, nome_produto, preço,tamanho):
        super().__init__(nome_produto, preço)
        self.tamanho = tamanho

pedido1 = PedidoEletronico("celular",5000,165)
print(pedido1.serial)