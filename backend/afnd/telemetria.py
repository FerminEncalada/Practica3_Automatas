def validar_telemetria(cadena):
    estados = {"q0"}

    for simbolo in cadena:
        nuevos = set()

        for estado in estados:
            if estado == "q0" and simbolo == "H":
                nuevos.add("q1")
            elif estado == "q1" and simbolo in ["T", "U"]:  # TEMP o HUM
                nuevos.add("q1")
            elif estado == "q1" and simbolo == "C":
                nuevos.add("qf")

        estados = nuevos

    return "qf" in estados