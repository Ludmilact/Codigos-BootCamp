
class Labirinto:

    PAREDE = '#'
    CAMINHO_LIVRE = ' '
    CAMINHO_PERCORRIDO = '-'
    ROBO = 'R'
    SAIDA = 'S'

    def __init__(self, mapa : list(list(str))):
        self.LABIRINTO : list(list(str)) = mapa

    def print_labirinto(self) -> None: 
        """
        Imprime o desenho do labirinto
        """

        print("")
        for linha in self.LABIRINTO:
            print("".join(linha))
        print("")