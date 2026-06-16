# senha = input("digite a senha: ")

# while senha != "senha123":
#     senha =input('digite novamente: ')
         
# print('acesso liberado')

contador = 0
soma = 0 

while contador < 5:
    numero = int(input(f'digite o {contador + 1}º numero: '))
    soma += numero
    contador += 1
media = soma/contador
print(f'a media dos numeros é {media}')

'''quantidade = 0

while quantidade < 5:
    print('Ola')
    quantidade += 1'''