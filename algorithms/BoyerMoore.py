def find(text, pattern):
    # Funcion auxiliar. Crea la tabla de bad character table
    def build_bad_char_table(pattern):
        # Inicializamos la tabla con -1 para todos los caracteres posibles
        bad_char_table = [-1] * 256
        # Recorremos el patron y guardamos la ultima posicion de cada caracter en la tabla
        for i in range(len(pattern)):
            bad_char_table[ord(pattern[i])] = i
        return bad_char_table

    m = len(pattern) # Longitud del patron
    n = len(text) # Longitud del texto

    # Construimos la bad character table para el patron
    bad_char_table = build_bad_char_table(pattern)
    
    # Lista para los índices donde hay coincidencias del patron
    indices = []
    
    s = 0 # Desplazamiento del patron sobre el texto

    # Mientras el patron pueda seguir desplazandose dentro del texto
    while s <= n - m:
        # Comenzamos a comparar desde el ultimo caracter del patron
        j = m - 1

        # Comparamos caracteres del patron y del texto mientras coincidan
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # Si se recorrio todo el patron, se encontro una coincidencia
        if j < 0:
            # Guardamos el indice de la coincidencia
            indices.append(s)
            # Movemos el patron hacia adelante con la bad character table
            s += (m - bad_char_table[ord(text[s + m])] if s + m < n else 1)
        else:
            # Si hay una falta de coincidencia, usamos la tabla para decidir cuantas veces mover el patron
            s += max(1, j - bad_char_table[ord(text[s + j])])

    # Devolvemos la lista de índices donde hubo coincidencias
    return indices
