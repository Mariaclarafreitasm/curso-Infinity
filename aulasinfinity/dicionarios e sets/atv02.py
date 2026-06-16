populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000}

nomePais = ""
maiorPopulacao = 0 

for nome, populacao in populacoes.items():
    if maiorPopulacao < populacao:
        maiorPopulacao = populacao
        nomePais = nome

print(f"O país {nomePais} tem a maior população de {maiorPopulacao} habitantes!")