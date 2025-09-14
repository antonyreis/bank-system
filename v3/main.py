from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Conta():
    def __init__(self, saldo, numero_conta, agencia, cliente, historico):
        self._saldo = saldo
        self._numero_conta = numero_conta
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls()
    
    def sacar(self, valor):
        return bool
    
    def depositar(self, valor):
        return bool

class ContaCorrente(Conta):
    def __init__(self, saldo, numero_conta, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero_conta, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    def realizar_transacao(self, conta, transacao):
        pass
    
    def adicionar_conta(self, conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
        
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, conta):
        pass
    
class Historico:
    def __init__(self):
        self._transacoes = []
        
    def adicionar_transacao(self, transacao):
        pass
