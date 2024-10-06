from helper_functions import dnaToProteinSequence  # Funcion auxiliar para traducir secuencias de ADN a proteinas

# Funcion que compara dos genomas y encuentra sus diferencias
def tarea4():
    genome1, genome2 = "", ""  # Variables para guardar las secuencias de los genomas

    # Leemos el archivo del genoma SARS-COV-2 de Wuhan 2019, ignorando las lineas que comienzan con ">"
    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome1 += line

    # Leemos el archivo del genoma SARS-COV-2 de Texas 2020, ignorando las lineas que comienzan con ">"
    with open("genomes/SARS-COV-2-MT106054.1.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome2 += line

    # Funcion para encontrar diferencias entre las dos secuencias a nivel de codones
    def find_differences(seq1, seq2):
        min_length = min(len(seq1), len(seq2))  # Determina la longitud minima de ambas secuencias
        
        differences = []  # Lista para guardar las diferencias encontradas
        
        # Recorremos ambas secuencias hasta la longitud minima
        for i in range(0, min_length):
            codon1 = seq1[i]  # Codon de la secuencia 1
            codon2 = seq2[i]  # Codon de la secuencia 2

            # Si los codones en la posicion actual son diferentes
            if codon1 != codon2:
                completeCodon1, completeCodon2 = "", ""  # Variables para guardar codones completos

                # Identificamos la posicion del codon completo (grupos de 3 nucleotidos)
                if i+1 % 3 == 1:
                    completeCodon1 = seq1[i-1:i+2]
                    completeCodon2 = seq2[i-1:i+2]
                elif i+1 % 3 == 2:
                    completeCodon1 = seq1[i-2:i+1]
                    completeCodon2 = seq2[i-2:i+1]
                else:
                    completeCodon1 = seq1[i:i+3]
                    completeCodon2 = seq2[i:i+3]

                # Traducimos los codones a secuencias de proteinas y metemos las diferencias a la lista
                differences.append((i, f"{dnaToProteinSequence.translate(completeCodon1)} ({completeCodon1})", f"{dnaToProteinSequence.translate(completeCodon2)} ({completeCodon2})"))

        # Manejar el caso donde una secuencia es mas larga que la otra
        if len(seq1) != len(seq2):
            longer_seq = seq1 if len(seq1) > len(seq2) else seq2
            for i in range(min_length, len(longer_seq), 3):
                codon = longer_seq[i:i+3]
                differences.append((i, codon, None))  # None significa que no hay codon correspondiente en la secuencia mas corta
                break  # Terminamos el ciclo despues de procesar el codon restante

        return differences  # Devolvemos las diferencias encontradas

    # Encontramos y guardamos las diferencias entre los dos genomas
    differences = find_differences(genome1, genome2)

    # Mostramos cada diferencia encontrada
    for diff in differences:
        print(diff)
