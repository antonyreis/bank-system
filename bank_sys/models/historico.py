from datetime import datetime

class Historico():
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "Operação": transacao.__class__.__name__,
            "Valor": transacao.valor,
            "Horário": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })