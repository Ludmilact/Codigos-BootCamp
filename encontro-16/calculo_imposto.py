
from impostos import *

class Venda:
    def __init__(self, valor_bruto: float, imposto: Imposto) -> None:
        self.valor_bruto = valor_bruto
        self.imposto = imposto
        self.valor_liquido = self.calcula_valor_liquido()
    
    def calcula_valor_liquido(self):
        if self.imposto == "ICMS":
            self.valor_liquido = self.valor_bruto * (1 - 0.05)
        
        if self.imposto == "IPI":
            self.valor_liquido = self.valor_bruto * (1 - 0.15)
        
        if self.imposto == "ISS":
            self.valor_liquido = self.valor_bruto * (1 - 0.10)
        
        return self.valor_liquido

vendas = Venda(1000, "ICMS")
print(vendas.calcula_valor_liquido())