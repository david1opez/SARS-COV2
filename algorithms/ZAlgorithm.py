# Complejidad: O(m + n)
def find(text, pattern):
    # Concatenamos el patron con un delimitador único ('$') y con el texto
    concat = pattern + '$' + text
    z = [0] * len(concat)  # Inicializamos el arreglo Z con ceros del tamaño de la cadena concatenada

    # Funcion para calcular el arreglo Z
    def calculate_z(concat):
        n = len(concat)
        left, right, k = 0, 0, 0  # Inicializamos los bordes del rango de la cadena concatenada (left y right)
        
        # Recorremos la cadena concatenada para calcular los valores Z
        for i in range(1, n):
            if i > right:  # Si cruzamos el borde del rango
                left, right = i, i
                # Expandimos el rango mientras los caracteres coincidan
                while right < n and concat[right] == concat[right - left]:
                    right += 1
                z[i] = right - left  # Longitud de la coincidencia
                right -= 1  # Ajustamos el borde right
            else:
                # Si estamos dentro del rango actual, usamos el valor Z ya calculado
                k = i - left
                if z[k] < right - i + 1:
                    z[i] = z[k]  # Copiamos el valor desde la posicion espejo
                else:
                    left = i  # Reajustamos el rango y lo alargamos
                    while right < n and concat[right] == concat[right - left]:
                        right += 1
                    z[i] = right - left
                    right -= 1

    # Llamamos a la funcion para llenar el arreglo Z
    calculate_z(concat)

    # Lista para guardar los indices donde el patron coincide con el texto
    indices = []
    pattern_len = len(pattern)  # Longitud del patron
    # Recorremos el arreglo Z para identificar coincidencias completas
    for i in range(pattern_len + 1, len(concat)):  # Empezamos despues del patron y el delimitador
        if z[i] == pattern_len:  # Si el valor Z es igual a la longitud del patron, entonces hay coincidencia
            indices.append(i - pattern_len - 1)  # Guardamos el indice en el texto original

    # Devolvemos los índices donde el patron se encontro en el texto
    return indices
