# mercado = {
#     "maçã": 3.50,
#     "leite": 4.80,
#     "pão": 2.00,
#     "café": 12.50
# }

# def calcular_total(dicionario:dict):
#     soma = 0
#     for i in dicionario.values():
#         soma+=i
#     return soma
# valor_total_sem_desconto = calcular_total(mercado)
    

# def aplicar_desconto(total,porcentagem=0.85):
#     return total - (total * porcentagem)

# valor_com_desconto = aplicar_desconto(toatal=valor_total_sem_desconto,porcentagem=0.85)



lista = [1,2,3,4,5]

lista_dobro = list(map(lambda x:x*2,lista))
print(lista_dobro)