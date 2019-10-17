class Conversor:
    TAM_PT_INTEIRA = 4
    TAM_PT_FRACIONARIA = 9
    NUM_BITS = 1 + TAM_PT_INTEIRA + TAM_PT_FRACIONARIA

    def decimal_para_binario(entrada):
        binario = []
        if entrada > 0:
            binario.append(0)
        else:
            binario.append(1)
            entrada *= -1
        p_interia, p_fracionaria = str(entrada).split(".")
        binario += Conversor.parte_inteira_para_binario(p_interia)
        binario += Conversor.parte_fracionaria_para_binario(p_fracionaria)
        return binario

    def parte_inteira_para_binario(entrada):
        entrada = int(entrada)
        binario = []
        while entrada != 0 and entrada != 1:
            bit = entrada % 2
            binario.insert(0, bit)
            entrada = entrada // 2
        binario.insert(0, entrada)
        while len(binario) != Conversor.TAM_PT_INTEIRA:
            binario.insert(0, 0)
        return binario

    def parte_fracionaria_para_binario(entrada):
        entrada = "0." + entrada
        entrada = float(entrada)
        binario = []
        for i in range(Conversor.TAM_PT_FRACIONARIA):
            entrada *= 2
            if entrada >= 1:
                binario.append(1)
                entrada = entrada % 1
            else:
                binario.append(0)
        return binario

    def binario_para_decimal(lista):
        valor = 0
        if lista[0] == 0:
            sinal = 1
        else:
            sinal = -1
        #
        indice = Conversor.TAM_PT_INTEIRA - 1
        for i in range(1, Conversor.NUM_BITS):
            bit = lista[i]
            valor += bit * 2 ** indice
            indice -= 1
        #
        valor *= sinal
        valor = round(valor, 2)
        return valor
