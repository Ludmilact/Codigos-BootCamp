from mailbox import NotEmptyError


class Funcionario:
    
    aumento_percentual: float = 0.10

    # método construtor
    def __init__(self, nome: str, sobrenome: str, salario_inicial: float = 1000):
        self.nome: str = nome 
        self.sobrenome: str = sobrenome
        self.__salario_inicial = salario_inicial
        self.email = f"{self.nome.lower()}.{self.sobrenome.lower().split()[-1]}@outlook.com"

    @property
    def salario_inicial(self):
        return self.__salario_inicial

    def dar_aumento(self) -> None:
        """
        Amplia o salário do funcionário em 10%.
        O novo salário será definido no atributo 'salario_atual'
        """
        if hasattr(self, "salario_atual"): # se eu tiver um salario pós aumento
            self.salario_atual = self.salario_atual * (1 + Funcionario.aumento_percentual)
        else: 
            self.salario_atual = self.salario_inicial * (1 + Funcionario.aumento_percentual)