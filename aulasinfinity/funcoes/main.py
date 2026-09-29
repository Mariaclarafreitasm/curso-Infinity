from calculos import calcular_media,calcular_soma

lista = [10,20,30,40]

lista_filtrada = list(filter(lambda x: x > 20,lista))
print(lista_filtrada)