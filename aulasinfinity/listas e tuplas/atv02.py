itens_add = int(input('quantos itens deseja adicionar: '))
mercado = []

for i in range(itens_add):
    item = input('digite qual o produto: ')
    mercado.append(item)

print(mercado)

remover = input('deseja remover algum item? ').lower()
if remover == 'sim' or remover == 's':
    produto_remover = input('qual produto quer remover: ')
    if produto_remover in mercado:
        mercado.remove(produto_remover)
    else:
        print('item não encontrado')
elif remover == 'não' or remover == 'n':
    print('boas compras')
else:
    print('digite uma resposta válida')

print(mercado)


 