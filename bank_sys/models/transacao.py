from ABC import abstractproperty, abstractmethod

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass
        
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        
        if sucesso:
            conta.historico.adicionar_transacao(self)
