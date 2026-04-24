def validar_cerradura(cadena):
    estado = "q0"

    for simbolo in cadena:
        if simbolo == "F":  # fallo
            if estado == "q0":
                estado = "q1"
            elif estado == "q1":
                estado = "q2"
            elif estado == "q2":
                estado = "bloqueado"
            else:
                estado = "bloqueado"
        elif simbolo == "O":  # correcto
            return True
        else:
            return False

    return estado != "bloqueado"