
import atividade3


class Teste:
    def teste():
        ponto = atividade3.Ponto(1, 1)
        print(ponto.qualQuadrante())
        quadrado = atividade3.Quadrilatero(3, 2)
        print(quadrado.contidoEmQ(ponto))


Teste.teste()