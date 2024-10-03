def longestPalindrome(s):
    # Añadimos # como separadores especiales para poder usar palindromes pares e impares de igual manera
    t = '#'.join(f'^{s}$')  # Añadimos ^ al inicio y $ al final para evitar desbordamientos
    n = len(t)  # Longitud de la nueva cadena transformada
    p = [0] * n  # Arreglo que guarda la longitud maxima de palindromo centrado en cada posicion
    center = 0  # El centro del palindromo mas largo que se conoce actualmente
    right = 0  # El limite derecho del palindromo mas largo conocido

    # Iteramos cada posicion en la cadena transformada excepto los extremos
    for i in range(1, n - 1):
        # Calculamos la posicion espejo de i respecto al centro actual
        mirror = 2 * center - i

        # Si estamos dentro de la longitud del palindromo actual, limitamos p[i] con la posicion espejo de i
        if i < right:
            p[i] = min(right - i, p[mirror])

        # Intentamos expandir el palindromo centrado en i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Si el palindromo en i cruza el limite derecho actual al expanderse, actualizamos center y right
        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Encontramos la longitud maxima del palindromo
    max_len = max(p)
    # Obtenemos el indice central de dicho palindromo
    center_index = p.index(max_len)

    # Calculamos el inicio del palindromo original en la cadena s
    start = (center_index - max_len) // 2
    return s[start: start + max_len]  # Devolvemos el palindromo mas largo
