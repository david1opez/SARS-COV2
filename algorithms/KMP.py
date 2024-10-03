# Complejidad: O(m + n)
def find(text, pattern):
    # Funcion auxiliar. Crea la tabla lps
    def build_lps(pattern):
        # Inicializamos con ceros, del mismo tamaño que el patron
        lps = [0] * len(pattern)
        length = 0  # Longitud del prefijo mas largo
        i = 1  # Comenzamos desde el segundo caracter

        # Mientras no hayamos recorrido todo el patron
        while i < len(pattern):
            # Si hay caracteres que coinciden, extendemos la longitud del prefijo y guardamos en lps
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                # Si no coinciden y length es mayor que 0, ajustamos length según la tabla lps
                if length != 0:
                    length = lps[length - 1]
                else:
                    # Si length es 0, se pone un 0 en la posición actual de lps y avanzamos
                    lps[i] = 0
                    i += 1
        return lps

    # Construimos la tabla lps para el patron
    lps = build_lps(pattern)
    
    # Lista para almacenar indices donde hay coincidencias
    indices = []
    i = 0  # Indice para el texto
    j = 0  # Indice para el patrón

    # Mientras no hayamos recorrido el texto por completo
    while i < len(text):
        # Si hay coincidencia de caracteres, avanzamos ambos indices
        if pattern[j] == text[i]:
            i += 1
            j += 1

        # Si hemos encontrado una coincidencia completa del patron
        if j == len(pattern):
            # Añadimos el indice donde comenzo la coincidencia
            indices.append(i - j)
            # Movemos j según la tabla LPS para ver si hay otras coincidencias
            j = lps[j - 1]
        # Si hay una falta de coincidencia despues de haber coincidido parcialmente
        elif i < len(text) and pattern[j] != text[i]:
            # Si no estamos en la posicion inicial del patron, ajustamos j segun la tabla LPS
            if j != 0:
                j = lps[j - 1]
            else:
                # Si estamos en la posicion inicial, simplemente avanzamos en el texto
                i += 1

    # Devolvemos los indices donde hubo coincidencias
    return indices
