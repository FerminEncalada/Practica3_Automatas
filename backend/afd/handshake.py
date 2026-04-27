"""
---------------------------------------------------------
Tema:
AFD - Protocolo Three Way Handshake

Lenguaje definido:
L = { SYA }

S = SYN
Y = SYN-ACK
A = ACK

Valida la sincronización correcta del protocolo.
---------------------------------------------------------
"""

def validar_handshake(cadena):
    """
    Simula un AFD para verificar la secuencia
    correcta del handshake.
    """

    estado="q0"

    for simbolo in cadena:

        # Transiciones del protocolo
        if estado=="q0" and simbolo=="S":
            estado="q1"

        elif estado=="q1" and simbolo=="Y":
            estado="q2"

        elif estado=="q2" and simbolo=="A":
            estado="qf"

        else:
            return False

    return estado=="qf"