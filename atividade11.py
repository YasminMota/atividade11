
import atividade3


class Teste:
    def teste():
        ponto = atividade3.Ponto(1, 1)
        print(ponto.qualQuadrante())
        quadrado = atividade3.Quadrilatero(5, 4)
        print(quadrado.contidoEmQ(ponto))


Teste.teste()