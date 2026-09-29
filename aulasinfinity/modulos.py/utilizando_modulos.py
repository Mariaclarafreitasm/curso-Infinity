from math import sqrt,factorial
import random
import datetime
import os

agora = datetime.datetime.now()
print(agora)

hoje = datetime.date.today()
print("Ano: ", hoje.year)

diretorio_atual = os.getcwd()
print(f"Diretorio de trabalho atual: {diretorio_atual}")





#n1 = int(input("digite um numero: "))
#print(sqrt(n1))
#print(factorial(n1))

#lista = ['maria','luis','lucas',"clara","mariana"]
#print(lista)
#print(random.choice(lista))
