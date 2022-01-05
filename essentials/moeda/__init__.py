def metade(dividir):
    dividir = dividir / 2
    return dividir


def dobro(dobrar):
    dobrar = dobrar * 2
    return dobrar


def aumento(aumentar, taxa=0):
    porcento = aumentar + (aumentar * taxa/100)
    return porcento


def diminui(diminuir, taxa=0):
    porcento2 = diminuir - (diminuir * taxa / 100)
    return porcento2
