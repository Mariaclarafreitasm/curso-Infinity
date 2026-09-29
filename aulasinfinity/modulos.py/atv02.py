import random
import math

filmes = [
    {
        "titulo": "Um Sonho de Liberdade",
        "ano": 1994,
        "duracao": 142,
        "nota_imdb": 9.3
    },
    {
        "titulo": "O Poderoso Chefão",
        "ano": 1972,
        "duracao": 175,
        "nota_imdb": 9.2
    },
    {
        "titulo": "Batman: O Cavaleiro das Trevas",
        "ano": 2008,
        "duracao": 152,
        "nota_imdb": 9.0
    },
    {
        "titulo": "Pulp Fiction: Tempo de Violência",
        "ano": 1994,
        "duracao": 154,
        "nota_imdb": 8.9
    }
]

print(len(filmes))

maior_imdb = 0
menor_nota = 10000
for i in filmes:
    if i["nota_imdb"] > maior_imdb:
        maior_imdb = i["nota_imdb"]

for i in filmes:
    if i["nota_imdb"] < menor_nota:
        menor_nota = i["nota_imdb"]

soma_notas = sum(filme["nota_imdb"] for filme in filmes)
media = soma_notas / len(filmes)
media = math.floor(media * 100) / 100

print(media)
print(random.choice(filmes))




print(maior_imdb)
print(menor_nota)