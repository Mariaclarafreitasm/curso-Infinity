quant_produtos = int(input("quantos produtos deseja cadastra?:  "))

for produto in range (quant_produtos):
    nome_produto = input("NOME DO PRODUTO:")
    quantidade = input("QUANTIDADE: ")
    print(f"PRODUTO:{nome_produto} | QUANTIDADE:{quantidade}")
