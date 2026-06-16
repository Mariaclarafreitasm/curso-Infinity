frutas = ('uva','laranja','morango','morango', 'morango', 'melancia','limão')

nomeFruta = input('digite o nome de uma fruta: ')
print(frutas)
if nomeFruta in frutas:
    print(f'{frutas.count(nomeFruta)} {nomeFruta}(s) disponível(eis)! ')
else:
    print(f'{nomeFruta} indisponível')





