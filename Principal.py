from Individuo import Individuo
from Geracao import Geracao

geracao_atual = Geracao()
print(geracao_atual)
for i in range(19):
    geracao_atual = Geracao(geracao_atual)
#    print(geracao_atual)
    print(geracao_atual.elite[0], geracao_atual.elite[0])
    print()
