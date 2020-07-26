def busca(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto)/2)
        chute = lista[meio]

        print("HISTORY: ", chute)

        if chute == item:
            return chute
        if meio > item:
            alto = meio - 1
        else:
            baixo = meio + 1


busca(range(0, 1000000), 8282)
