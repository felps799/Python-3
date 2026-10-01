def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: Mostrar, ou não, o processo
    :return: O valor do Fatorial de um número numero.
    """
    fatorial = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= c
        c =-1
    return fatorial

print(fatorial(5, show=True))
help(fatorial)