import Despesas.py
import Receitas.py


class Saldo(Despesas, Receitas):
    def __init__(self, valorSomar, valorSubtrair):
        super().__init__(valorSomar)
        super().__init__(valorSubtrair)
        self.valorSomar = valorSomar
        self.valorSubtrair = valorSubtrair
        self.valorTotal = self.valorSomar - self.valorSubtrair
