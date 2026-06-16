# dicionarios
# "super variaveis"
# armazenam mais de um valor por vez
# objetos iteraveis
# colecoes de dados
# sao posiconados atraves de chaves nomeadas
# a ordem de insercao nao importa
# a insercao do dado é feita no par chave: valor
# os nomes das chaves sao unicos
# as chaves podem ser - strings, numeros ou tuplas
# os valores podem ser - qualquer coisa
# dicionarioVazio = {}
# dicionarioVazio2 = dict()
# dados = {
#     "nome": "Antonio",
#     "idade": 30,
#     "altura": 1.73,
#     "cnh": True
# }
# print(dados)
# # acessando itens
# # busca não segura
# print(dados["nome"])
# # busca segura com condicional if
# if "nome1" in dados:
#     print(dados["nome"])
# else:
#     print("Chave não encontrada!")
# # busca segura mais eficiente com o metodo .get()
# print(dados.get("nome1", "Chave não identifcada!!!"))
# print("-"*50)
# # alterando
# dados["cnh"] = False
# print(dados)
# # add
# dados["estado_civil"] = "Solteiro"
# print(dados)
# dados.update(nacionalidade="Brasileiro", naturalidade="Soteropolitano")
# print(dados)
# print("-"*50)
# # excluir
# print(dados.pop("cnh"))
# print(dados)
# del dados["altura"]
# print(dados)
# # dados.clear()
# # print(dados)
# print("-"*50)
# # percorrendo dicionarios
# # percorrendo chave e valor mas mostrando só a chave
# for d in dados:
#     print(d)
# print("-"*50)

# # percorrendo chave e mostrando só a chave
# for d in dados.keys():
#     print(d)
# print("-"*50)

# # percorrendo valor e mostrando só o valor
# for d in dados.values():
#     print(d)
# print("-"*50)

# # percorrendo tudo e mostrando tudo
# for chave, valor in dados.items():
#     print(f"{chave} - {valor}")
# print("-"*50)

# sets (conjuntos)
# "super variaveis"
# armazenam mais de um valor por vez
# objetos iteraveis
# colecoes de dados
# a ordem de insercao nao importa
# não sao posicionados, nao tem
# randomico
# nao armazenam valores duplicados
# sao mais rapidos de acessar do que as outras estruturas
conjuntoVazio = set()
frutas = {"uva", "pera", "maca", "uva"}
print(frutas)
print("-"*50)
# add
frutas.add("morango")
print(frutas)
frutas.update(("amora", "abacaxi"))
print(frutas)
print("-"*50)
# excluir
frutas.remove("uva") # remove, caso nao encontre retorna erro
print(frutas)
frutas.discard("abacaxi") # remove, caso nao encontre ignora e segue o codigo
print(frutas)
print(frutas.pop()) # remove aleatorio
print(frutas)
print("-"*50)
# operacoes
frutas = {"uva", "pera", "maca", "uva"}
frutas2 = {"amora", "kiwi", "uva"}
frutas3 = frutas - frutas2
frutas4 = frutas.difference(frutas2)
print(frutas3)
print(frutas4)
print("-"*50)
frutas5 = frutas | frutas2
frutas6 = frutas.union(frutas2)
print(frutas5)
print(frutas6)
print("-"*50)
frutas7 = frutas ^ frutas2
frutas8 = frutas.symmetric_difference(frutas2)
print(frutas7)
print(frutas8)
print("-"*50)
frutas9 = frutas & frutas2
frutas10 = frutas.intersection(frutas2)
print(frutas9)
print(frutas10)
print("-"*50)