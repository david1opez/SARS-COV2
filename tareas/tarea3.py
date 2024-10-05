import time
from algorithms import ZAlgorithm
from helper_functions import expasy

def tarea3():
    genome = ""

    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome += line

    genomeProteinSequence = expasy.translate(genome)

    startTime = time.time()

    print(len(genome))
    print(len(genomeProteinSequence))

    with open("seq-proteins.txt") as file:
        for line in file.read().splitlines():
            if line[0] == ">":
                print("\nProteína:", line.replace(">", ""))
            else:
                genomeIndices = ZAlgorithm.find(genomeProteinSequence, line)

                if(len(genomeIndices) > 0):
                    print("Indices en el genoma:", genomeIndices)
                    print("Secuencia de aminoácidos:", genomeProteinSequence[genomeIndices[0]:genomeIndices[0]+4])
                else:
                    print("No se encontró la secuencia de aminoácidos en el genoma")

    
    print("\nTiempo de ejecución:", round((time.time() - startTime) * 1000, 2), "ms")