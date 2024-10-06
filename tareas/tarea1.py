import time
from algorithms import KMP, BoyerMoore

# Funcion que recibe el nombre del algoritmo a utilizar
def tarea1(algorithm):
    executionTime = 0.0  # Variable para guardar el tiempo de ejecucion
    genome = ""  # Variable para guardar el genoma completo
    genM, genORF1AB, genS = "", "", ""  # Variables para guardar los genes especificos

    # En esta seccion leemos y guardamos el contenido de los archivos ignorando las lineas que comienzan con ">"
    # Archivo 'gen-M.txt'
    with open("genes/gen-M.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genM += line
        
    # Archivo 'gen-ORF1AB.txt',
    with open("genes/gen-ORF1AB.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genORF1AB += line
    
    # Archivo 'gen-S.txt'
    with open("genes/gen-S.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genS += line
        
    # Archivo del genoma completo SARS-COV-2
    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome += line

    
    # En esta seccion usamos los algoritmos para buscar los genes en el genoma
    # Algoritmo BoyerMoore
    if algorithm == "BoyerMoore":
        startTime = time.time()  # Usamos el cronometro

        # Buscamos los genes M, ORF1AB y S en el genoma
        indicesM = BoyerMoore.find(genome, genM)
        indicesORF1AB = BoyerMoore.find(genome, genORF1AB)
        indicesS = BoyerMoore.find(genome, genS)

        executionTime = time.time() - startTime  # Calcula el tiempo de ejecucion
    # Algoritmo KMP
    else:
        startTime = time.time()  # Usamos el cronometro

        # Buscar los genes M, ORF1AB y S en el genoma
        indicesM = KMP.find(genome, genM)
        indicesORF1AB = KMP.find(genome, genORF1AB)
        indicesS = KMP.find(genome, genS)

        executionTime = time.time() - startTime  # Calcula el tiempo de ejecucion

    # Resultados para el gen S
    print("Gen S")
    print("Indices de aparición: ", indicesS)
    print("Primeros 12 caracteres: ", genome[indicesS[0]:indicesS[0]+12])

    # Resultados para el gen M
    print("\nGen M")
    print("Indices de aparición: ", indicesM)
    print("Primeros 12 caracteres: ", genome[indicesM[0]:indicesM[0]+12])

    # Resultados para el gen ORF1AB
    print("\nGen ORF1AB")
    print("Indices de aparición: ", indicesORF1AB)
    print("Primeros 12 caracteres: ", genome[indicesORF1AB[0]:indicesORF1AB[0]+12])

    # Tiempo total de ejecucion
    print("\nTiempo de ejecución del algoritmo: ", round(executionTime*1000,1), "ms")
