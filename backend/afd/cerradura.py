"""
---------------------------------------------------------
Tema:
AFD - Cerradura Inteligente

Lenguaje:
Intentos fallidos y acceso válido.

F = intento fallido
O = acceso correcto

Tres fallos consecutivos bloquean el sistema.
---------------------------------------------------------
"""

def validar_cerradura(cadena):
    """
    Simula el comportamiento de una cerradura
    que registra errores mediante estados.
    """

    estado="q0"

    for simbolo in cadena:

        # Gestión de fallos consecutivos
        if simbolo=="F":

            if estado=="q0":
                estado="q1"

            elif estado=="q1":
                estado="q2"

            elif estado=="q2":
                return False

        # Apertura correcta
        elif simbolo=="O":
            return True

        else:
            return False

    return estado!="bloqueado"