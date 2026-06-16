proriginal = int(input('valor original do produto? '))
quantidade = int(input('qual foi a quantidade? '))
desconto = 0.10
valor_total = proriginal*quantidade


if quantidade > 10: 
    print('desconto de 10% aplicado')
    print(valor_total-(valor_total*desconto))
else:
    print('sem desconto')
