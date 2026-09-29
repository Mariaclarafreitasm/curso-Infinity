lista = [1,2,3,4,5]
lista_nomes = ["joao","ana","pedro"]

def processar_lista(lista,funcao):
    return [funcao(i) for i in lista]

def maiusculo(x:str):
    return x.capitalize()

def dobro(x):
    return x *2 

def acrescentar(x):
    return x +5

lista_dobrada = processar_lista(lista,dobro)

print(processar_lista(lista_nomes,maiusculo))
