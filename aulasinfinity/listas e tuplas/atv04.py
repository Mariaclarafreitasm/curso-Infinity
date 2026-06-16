notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]

media = sum(notas_brutas)/len(notas_brutas)
print(media)

notas_aprovadas = [n for n in notas_brutas if n >= 7]
print(notas_aprovadas)