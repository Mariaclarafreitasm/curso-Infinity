class Motor:
    def __init__(self,potencia):
        self.__potencia = potencia
       

    @property
    def potencia(self):
      return self.__potencia

    @potencia.setter
    def potencia(self):
        if self.__potencia >= 0:
            return print("Motor potente!")

class Carro:
   def __init__(self,marca):
      self.marca = marca
      self.motor = Motor(1000)

carro1 = Carro("celta")
print(carro1.motor.potencia)