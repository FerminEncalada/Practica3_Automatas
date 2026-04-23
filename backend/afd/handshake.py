def validar_handshake(cadena):
    estado = "q0"

    for simbolo in cadena:
        if estado == "q0" and simbolo == "S":      # SYN
            estado = "q1"
        elif estado == "q1" and simbolo == "Y":    # SYN-ACK
            estado = "q2"
        elif estado == "q2" and simbolo == "A":    # ACK
            estado = "qf"
        else:
            return False

    return estado == "qf"