class Conta:
    def __init__(self, titular, numero):
        self._saldo = 0.0
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = saldo

    def saque(self, valor):
        if valor <= 0:
            print("O valor de saque deve ser maior que zero.")
        elif self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")
        
    def deposita(self, valor):
        if valor <= 0:
            print("O valor de depósito deve ser maior que zero.")
        else:
            self.saldo += valor

    def extrato(self):
        print(f"Cliente: {self._titular}, Saldo atual: R$ {self._saldo:.2f}")
