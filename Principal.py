from Individuo import Individuo
from Geracao import Geracao

geracao_atual = Geracao()
print(geracao_atual)
for i in range(2, 21):
    geracao_atual = Geracao(geracao_atual)
    print("Geracao", i)
    print(geracao_atual.elite[0])
    print()
