class Lampada:
    material = "vidro"
    def __init__(self):
        self.ligada = False
    def ligar(self):
        self.ligada = True
    
        print("Lampada ligada!")
    def desligar(self):
        self.desligar = False
        print("Lampada desligada!")
    def verificar_estado(self):
        if self.ligada == True:
            print("esta ligada")
        else:
            print("desligada")