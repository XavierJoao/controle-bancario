from Cliente import Cliente
from Conta import Conta

class Main:
    def __init__(self):
        self.executar()

    def executar(self):
        c1 = Cliente("João", "1198765-4321")
        conta = Conta(c1.nome, 6565)

        conta.deposita(100)
        conta.saque(50)
        conta.extrato()

if __name__ == "__main__":
    Main()
