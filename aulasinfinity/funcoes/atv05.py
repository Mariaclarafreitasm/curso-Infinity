def executar_pipeline(lista,funcao):
    return [funcao(i) for i in lista]

def dobro(x):
    return x *2

def acrescentar(x):
    return x +5
