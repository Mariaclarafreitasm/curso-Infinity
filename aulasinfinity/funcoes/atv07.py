def cadastro():
    produtos = {
    "Camiseta": 50.00,
    "Tênis": 200.00,
    "Boné": 40.00,
    "Mochila": 120.00,
    "Jaqueta": 300.00
    }
    return produtos
diconario = cadastro()

def valor_total(produto,quantidade,dicionario):
    return dicionario[produto] * quantidade

def desconto(valor,tipo):
    
    if tipo=="pix":
        return valor - (valor * 0.90)
    elif tipo=="debito":
        return valor - (valor * 0.95)
    elif tipo =="credito":
        return valor

def processar_venda(produto,quantidade,tipo_pagamento,valor_com_desconto):
    print(f"produto: {produto} | quantidade : {quantidade} | pagamento {tipo_pagamento} | valor final {valor_com_desconto}")