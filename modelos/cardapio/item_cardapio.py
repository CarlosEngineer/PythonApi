from abc import ABC, abstractmethod 

class itemCardapio(ABC):
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = float(preco)


    def __str__(self):
        return self.nome
    
    @abstractmethod
    def aplicar_desconto(self):
        pass
