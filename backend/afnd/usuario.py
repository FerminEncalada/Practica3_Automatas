def validar_usuario(cadena):
    estados = {"q0"}

    for simbolo in cadena:
        nuevos = set()

        for estado in estados:
            if estado == "q0" and simbolo == "H":
                nuevos.add("q1")
            elif estado == "q1" and simbolo == "S":
                nuevos.add("q2")
            elif estado == "q2" and simbolo == "S":
                nuevos.add("q2")
            elif estado == "q2" and simbolo == "C":
                nuevos.add("qf")

        estados = nuevos

    return "qf" in estados