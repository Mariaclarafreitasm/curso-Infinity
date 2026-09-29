class Tarefa:
    def __init__(self,titulo,prioridade=False):
        self.titulo = titulo
        self.prioridade = prioridade

    def marcar_concluida(self):
        if self.prioridade == False:
            self.prioridade = True
            return self.prioridade

tarefa1 = Tarefa("estudar")
print(tarefa1.prioridade)
tarefa1.marcar_concluida()
print(tarefa1.prioridade)

