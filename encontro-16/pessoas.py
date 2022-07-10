class Funcionario:

    aumento_percentual: float = 0.1

    # DOIS UNDELINES!
    # METODO CONSTRUTOR!

    def __init__(self, nome: str, sobrenome: str, salario_inicial: int):
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self._salario_inicial = salario_inicial
        self.email = f"{self.nome.lower()}.{self.sobrenome.lower().split()[-1]}@email.com"