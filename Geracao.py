from Individuo import Individuo

class Geracao:
    TAMANHO = 30
    NUM_GRUPOS = 5

    def __init__(self, geracao_passada=None):
        if geracao_passada == None:
            self.individuos = []
            for i in range(self.TAMANHO):
                self.individuos.append(Individuo())
        else:
            self.selecionar(geracao_passada)
#            self.crossover()
#            self.mutacao()

    def selecionar(self):
        pass

    def __str__(self):
        representacao = ""
        for individuo in self.individuos:
            representacao += str(individuo)
            representacao += "\n"
        representacao += "\n"
        return representacao
