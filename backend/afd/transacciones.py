"""
---------------------------------------------------------
Tema:
Autómata Finito Determinista (AFD)
Validador de Flujo de Transacciones Bancarias

Lenguaje definido:
L = { ACL }

Reconoce únicamente secuencias con el patrón:
Autorización -> Captura -> Liquidación

A = Autorización
C = Captura
L = Liquidación
---------------------------------------------------------
"""

def validar_transaccion(cadena):
    """
    Evalúa si una cadena pertenece al lenguaje del AFD.
    
    Función:
    Simula las transiciones entre estados para validar
    que la secuencia siga el orden correcto.
    """

    # Estado inicial del autómata
    estado = "q0"

    # Recorrido secuencial de símbolos de entrada
    for simbolo in cadena:

        # Transiciones válidas del autómata
        if estado=="q0" and simbolo=="A":
            estado="q1"

        elif estado=="q1" and simbolo=="C":
            estado="q2"

        elif estado=="q2" and simbolo=="L":
            estado="qf"

        # Si no existe transición válida, se rechaza
        else:
            return False

    # Acepta solo si termina en estado final
    return estado=="qf"