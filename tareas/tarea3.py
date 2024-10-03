import time
from algorithms import ZAlgorithm
from helper_functions import dnaToProteinSequence

def tarea3():
    genome = ""

    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome += line

    genomeProteinSequence = dnaToProteinSequence.translate(genome)

    startTime = time.time()

    with open("seq-proteins.txt") as file:
        for line in file.read().splitlines():
            if line[0] == ">":
                print("Proteína:", line.replace(">", ""))
            else:
                genomeIndices = ZAlgorithm.find(genomeProteinSequence, line)

                if(len(genomeIndices) > 0):
                    print("\nIndices en el genoma:", genomeIndices)
                    print("Secuencia de aminoácidos:", genomeProteinSequence[genomeIndices[0]:genomeIndices[0]+4])
                    print("Secuencia de codones:", genome[genomeIndices[0]*3:genomeIndices[0]*3+12])
                else:
                    print("\nNo se encontró la secuencia de aminoácidos en el genoma")
    
    print("\nTiempo de ejecución:", round((time.time() - startTime) * 1000, 2), "ms avg.")