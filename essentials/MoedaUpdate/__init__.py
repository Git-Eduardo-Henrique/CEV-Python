def metade(dividir=0.0, formato=False):
    res = dividir / 2
    return res if not formato else tipo(res)


def dobro(dobrar=0.0, formato=False):
    res = dobrar * 2
    return res if not formato else tipo(res)


def aumento(aumentar=0.0, taxa=0.0, formato=False):
    res = aumentar + (aumentar * taxa / 100)
    return res if not formato else tipo(res)


def diminui(diminuir=0.0, taxa=0.0, formato=False):
    res = diminuir - (diminuir * taxa / 100)
    return res if not formato else tipo(res)


def tipo(preco=0.0, moeda="R$"):
    return F"{moeda}{preco:.2f}".replace('.', ',')


def resumo(p, taxa1=0.0, taxa2=0.0, formato=False):
    print(f"Dobro: \t{dobro(p, formato)}")
    print(f"Metade: \t{metade(p, formato)}")
    print(f"aumento de {taxa1}% : \t{aumento(p, taxa=taxa1, formato=formato)}")
    print(f"diminuiçao de {taxa2}%: \t{diminui(p, taxa=taxa2, formato=formato)}")