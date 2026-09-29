from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = reduce(lambda x,y: x+y,numeros)
print(numero)

lista_dobro = list(map(lambda x:x*2,numeros))
print(lista_dobro)
def pares(numeros):
    par = []
    for numero in numeros:
        if numero % 2 == 0:
            par.append(numero)
    return par

print(pares(numeros))

pares2 = list(filter(lambda x: x % 2 == 0,numeros ))
print(pares2)