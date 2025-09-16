class Conta():
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(numero_conta, cliente)
    
    def sacar(self, valor):
        saldo = self.saldo
        sucesso = True
        if saldo <= 0 or valor > saldo:
            sucesso = False
        else: 
            self._saldo -= valor
        
        return sucesso
    
    def depositar(self, valor):
        sucesso = True
        if valor <= 0:
            sucesso = False
        else: 
            self._saldo += valor
        
        return sucesso

class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        saques_realizados = len([transacao for transacao in self.historico.transacoes if transacao["Operação"] == Saque.__name__])
        
        if valor > self.limite or saques_realizados >= self.limite_saques:
            return False
        
        return super().sacar(valor)
    
    def __str__(self):
        return f"""
            Agência:\t {self.agencia}
            C/C:\t {self.numero_conta}
            Titular:\t {self.cliente.nome}
        """
