class Aluno:
    def __init__(self,nome,idade,matricula):
       self.nome = nome
       self.idade = idade
       self.__matricula = matricula 

    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula): 
        self.__matricula = matricula
    

aluno1 = Aluno("maria", 19, "20261001")


print("Nome:", aluno1.get_nome())
print("Idade:", aluno1.get_idade())
print("Matrícula:", aluno1.get_matricula())


aluno1.set_matricula(3131312)
print("Nova matricula:", aluno1.get_matricula())