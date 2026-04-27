"""
---------------------------------------------------------
Tema:
AFND - Comprador Potencial en E-commerce

Lenguaje:
L = { H S^n C | n >= 1 }

Patrón:
HOME SEARCH + CART
---------------------------------------------------------
"""

def validar_usuario(cadena):
    """
    Modela comportamiento de navegación del usuario
    mediante autómata no determinista.
    """

    estados={"q0"}

    for simbolo in cadena:

        nuevos=set()

        for estado in estados:

            if estado=="q0" and simbolo=="H":
                nuevos.add("q1")

            if estado=="q1" and simbolo=="S":
                nuevos.add("q2")

            # Repetición SEARCH+
            if estado=="q2" and simbolo=="S":
                nuevos.add("q2")

            if estado=="q2" and simbolo=="C":
                nuevos.add("qf")

        estados=nuevos

    return "qf" in estados