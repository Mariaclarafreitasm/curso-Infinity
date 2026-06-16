vendas = {"Ana": 10, "Bruno": 15, "Carla": 8}
print(vendas)
print("-"*50)

vendas["Pedro"] = 12
print(vendas)
print("-"*50)

del vendas["Carla"]
print(vendas)
print("-"*50)

soma = 0

for v in vendas.values():
    soma += v
print(f"SOMA TOTAL DAS VENDAS \n{soma} vendas")
