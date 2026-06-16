# nome = str(input('digite seu nome completo: '))
# idade = int(input('digite sua idade: '))
# salario = float(input('digite seu salario mensal: '))
# salario_anual = salario * 12

# if idade >=18:
#     print('funcionario maior de idade')
#     print(f'RELATÓRIO \n idade = {idade} \n nome = {nome} \n salário anual = {salario_anual}')

#indices    0       1         2     3       4           5           6       7
# frutas = ['maçã', 'banana', 'uva', 'pera', 'sapoti', 'abacate', 'mamão', 'morango']

# # start, stop, step no fatiamento de lista
# frutas2 = frutas[0:2]
# print (frutas2)
# frutas3 = frutas[1:3]
# print (frutas3)
# frutas4 = frutas[1:6:2]
# print (frutas4)
# frutas5 = frutas[::2]
# print (frutas5)
# frutas6 = frutas[::-1]
# print (frutas6)

# # texto = tuple('Daniel')
# texto = ['Daniel']
# print(texto[::-1])
# print(texto[0])


frutas = ['Maçã', 'banana', 'Uva', 'pera', 'sapoti', 'banana', 'abacate', 'Mamão', 'Morango', 'banana', 'banana']

frutas.append('kiwi')
print(frutas)
frutas.insert(2, 'melancia')
print(frutas)
frutas.remove('banana')
print(frutas)
frutas.pop()
print(frutas)
frutas.pop(4)
print(frutas)
# frutas.sort()
# print(frutas)
frutas.reverse()
print(frutas)
print(frutas.count('banana'))
print(frutas.index('Morango'))