def validar_genetica(cadena):
    estados = {"q0"}

    for simbolo in cadena:
        nuevos = set()

        for estado in estados:
            if estado == "q0" and simbolo == "K":
                nuevos.add("q1")
            elif estado == "q1" and simbolo == "G":
                nuevos.add("q2")
            elif estado == "q2" and simbolo == "X":
                nuevos.add("q2")
            elif estado == "q2" and simbolo == "F":
                nuevos.add("qf")

        estados = nuevos

    return "qf" in estados