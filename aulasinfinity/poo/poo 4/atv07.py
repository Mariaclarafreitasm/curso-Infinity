from abc import ABC,abstractmethod
class Publicacao(ABC):
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    @abstractmethod
    def exibir_info(self):
        print(f"o titulo é  {self.titulo} e o autor {self.autor}")
    
class Livro(Publicacao):
    def __init__(self, titulo, autor,pagina_livro):
        self.pagina = pagina_livro
        super().__init__(titulo, autor)
    def exibir_info(self):
        print(f" {super.exibir_info()} e esta na pagina {self.pagina}")

class Revista(Publicacao):
    def __init__(self, titulo, autor,edicao):
        self.edicao = edicao
        super().__init__(titulo, autor)
    def exibir_info(self):
        print(f" {super.exibir_info()} e a edição do livro: {self.edicao}")