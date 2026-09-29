def analisar_notas(*notas):
    notas_diconario = {}
    nota_maior = 0
    menor_nota = 1000
    for nota in notas:
        if nota > nota_maior:
            nota_maior = nota
    for nota in notas:
        if nota < menor_nota:
            menor_nota = nota
    # max(notas)
    # min(notas)
    notas_diconario["maior_nota"] = nota_maior
    notas_diconario["menor_nota"] = menor_nota
    notas_diconario["media"] = sum(notas)/len(notas)
    return notas_diconario

print(analisar_notas(10,3,5,6,7))

    