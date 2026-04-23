def validar_transaccion(cadena):
    estado = "q0"

    for simbolo in cadena:
        if estado == "q0" and simbolo == "A":
            estado = "q1"
        elif estado == "q1" and simbolo == "C":
            estado = "q2"
        elif estado == "q2" and simbolo == "L":
            estado = "qf"
        else:
            return False

    return estado == "qf"