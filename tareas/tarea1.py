import time
from algorithms import KMP, BoyerMoore

def tarea1(algorithm):
    executionTime = 0.0
    genome = ""
    genM, genORF1AB, genS = "", "", ""

    with open("genes/gen-M.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genM += line
        
    with open("genes/gen-ORF1AB.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genORF1AB += line
    
    with open("genes/gen-S.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genS += line
        
    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome += line

    if algorithm == "BoyerMoore":
        startTime = time.time()

        indicesM = BoyerMoore.find(genome, genM)
        indicesORF1AB = BoyerMoore.find(genome, genORF1AB)
        indicesS = BoyerMoore.find(genome, genS)

        executionTime = time.time() - startTime
    else:
        startTime = time.time()

        indicesM = KMP.find(genome, genM)
        indicesORF1AB = KMP.find(genome, genORF1AB)
        indicesS = KMP.find(genome, genS)

        executionTime = time.time() - startTime

    print("Gen S")
    print("Indices de aparición: ", indicesS)
    print("Primeros 12 caracteres: ", genome[indicesS[0]:indicesS[0]+12])

    print("\nGen M")
    print("Indices de aparición: ", indicesM)
    print("Primeros 12 caracteres: ", genome[indicesM[0]:indicesM[0]+12])

    print("\nGen ORF1AB")
    print("Indices de aparición: ", indicesORF1AB)
    print("Primeros 12 caracteres: ", genome[indicesORF1AB[0]:indicesORF1AB[0]+12])

    print("\nTiempo de ejecución del algoritmo: ", round(executionTime*1000,1), "ms")