from helper_functions import dnaToProteinSequence

def tarea4():
    genome1, genome2 = "", ""

    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome1 += line

    with open("genomes/SARS-COV-2-MT106054.1.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome2 += line

    def find_differences(seq1, seq2):
        # Determinar la longitud de la secuencia más corta
        min_length = min(len(seq1), len(seq2))
        
        differences = []
        
        # Comparar los codones (substrings de 3 caracteres)
        for i in range(0, min_length, 3):
            codon1 = dnaToProteinSequence.translate(seq1[i:i+3])
            codon2 = dnaToProteinSequence.translate(seq2[i:i+3])
            
            if codon1 != codon2:
                differences.append((i, codon1, codon2))

        # Manejar caracteres restantes en la secuencia más larga
        if len(seq1) != len(seq2):
            longer_seq = seq1 if len(seq1) > len(seq2) else seq2
            for i in range(min_length, len(longer_seq), 3):
                codon = dnaToProteinSequence.translate(longer_seq[i:i+3])
                differences.append((i, codon, None))  # None para el codón faltante

        return differences

    differences = find_differences(genome1, genome2)
    for diff in differences:
        print(diff)
