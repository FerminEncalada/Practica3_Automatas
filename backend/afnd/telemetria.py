"""
---------------------------------------------------------
Tema:
AFND - Validación de Telemetría IoT

Lenguaje:
L = H (T|U)* C

H = HDR
T = TEMP
U = HUM
C = CRC
---------------------------------------------------------
"""

def validar_telemetria(cadena):
    """
    Simula validación de paquetes IoT
    mediante un AFND.
    """

    estados={"q0"}

    for simbolo in cadena:

        nuevos=set()

        for estado in estados:

            if estado=="q0" and simbolo=="H":
                nuevos.add("q1")

            # Unión (TEMP | HUM)
            if estado=="q1" and simbolo=="T":
                nuevos.add("q1")

            if estado=="q1" and simbolo=="U":
                nuevos.add("q1")

            # Cierre CRC
            if estado=="q1" and simbolo=="C":
                nuevos.add("qf")

        estados=nuevos

    return "qf" in estados