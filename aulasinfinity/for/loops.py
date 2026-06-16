# while - percorrer iteracoes controladas pelo usuario
# condicao de entrada - so funciona mediante condicoes verdadeiras
# condicao de saida - encerra transformando o True em False
# sem condicao de saida vira loop infinito

# for - percorrer iteracoes com tamanhos já definidos
# mais eficiente do que while
# sintaxe:
# for variavel in sequencia:
#     bloco de codigo
# sequencia - strings, listas, tuplas, sets ou dicionarios
# for percorrento strings serve para operacoes de buscas e filtragens
# nome = "Antonio"
# for letra in nome:
#     print(letra)

# nome = input("Digite seu nome: ")
# for letra in nome:
#     print(letra)

# palavra = input("Digite uma palavra: ")
# vogais = "aeiouáéíóúâêîôûãõ"
# total_vogais = 0
# for letra in palavra:
#     if letra.isalpha():
#         if letra.lower() in vogais:
#             total_vogais += 1
# print(f"A quantidade de vogais da palavra {palavra} é: {total_vogais}")

# range(start, stop, step) - simula uma sequencia numerica posicionada atraves de indices numericos
# start - opcional - em qual indice voce quer começar, padrao 0
# stop - obrigatorio - em qual indice voce quer parar, excluindo-o
# step - opcional - de quanto em quanto, passo, incremendo, decremento, padrao 1

# print("-"*50)
# print("*** COM PARAMETRO STOP ***")
# for r in range(5):
#     print(r)

# print("-"*50)
# print("*** COM PARAMETROS START E STOP ***")
# for r in range(1, 5):
#     print(r)

# print("-"*50)
# print("*** COM PARAMETROS START, STOP E STEP ***")
# for r in range(1, 11, 2):
#     print(r)

# print("-"*50)
# print("*** COM PARAMETROS START, STOP E STEP ***")
# for r in range(10, 0, -1):
#     print(r)

# aninhamento de laço for

# for r in range(4):
#     for i in range(2):
#         print(f"{r} - {i}")