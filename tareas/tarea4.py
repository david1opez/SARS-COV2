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
        min_length = min(len(seq1), len(seq2))
        
        differences = []
        
        for i in range(0, min_length):
            codon1 = seq1[i]
            codon2 = seq2[i]

            if codon1 != codon2:
                completeCodon1, completeCodon2 = "", ""

                if i+1 % 3 == 1:
                    completeCodon1 = seq1[i-1:i+2]
                    completeCodon2 = seq2[i-1:i+2]
                elif i+1 % 3 == 2:
                    completeCodon1 = seq1[i-2:i+1]
                    completeCodon2 = seq2[i-2:i+1]
                else:
                    completeCodon1 = seq1[i:i+3]
                    completeCodon2 = seq2[i:i+3]

                differences.append((i, f"{dnaToProteinSequence.translate(completeCodon1)} ({completeCodon1})", f"{dnaToProteinSequence.translate(completeCodon2)} ({completeCodon2})"))

        # Manejar caracteres restantes en la secuencia más larga
        if len(seq1) != len(seq2):
            longer_seq = seq1 if len(seq1) > len(seq2) else seq2
            for i in range(min_length, len(longer_seq), 3):
                codon = longer_seq[i:i+3]
                differences.append((i, codon, None))  # None para el codón faltante
                break

        return differences

    differences = find_differences(genome1, genome2)
    for diff in differences:
        print(diff)
