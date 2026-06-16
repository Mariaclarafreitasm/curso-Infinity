produtos = [('banana', 2.5), ('maçã', 4.0), ('laranja', 3.0)]

produtos02 = {'banana':2.5,'maçâ':4.0,'laranja':3.0}
for chave, valor in produtos02.items():
    print(f"o preço da {chave} é R${valor}")
