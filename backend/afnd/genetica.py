"""
---------------------------------------------------------
Tema:
AFND - Reconocimiento de Secuencias Genéticas

Lenguaje:
L = { K G X^n F | n >= 0 }

Patrón:
K G X* F

X representa cualquier aminoácido repetido
cero o más veces.
---------------------------------------------------------
"""

def validar_genetica(cadena):
    """
    Simula un AFND usando conjunto de estados activos.
    Reconoce patrones genéticos definidos.
    """

    estados={"q0"}

    for simbolo in cadena:

        nuevos=set()

        # Evaluación de transiciones posibles
        for estado in estados:

            if estado=="q0" and simbolo=="K":
                nuevos.add("q1")

            if estado=="q1" and simbolo=="G":
                nuevos.add("q2")

            # Clausura de Kleene X*
            if estado=="q2" and simbolo=="X":
                nuevos.add("q2")

            # Estado de aceptación
            if estado=="q2" and simbolo=="F":
                nuevos.add("qf")

        estados=nuevos

    # Se acepta si algún camino llega a qf
    return "qf" in estados