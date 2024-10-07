import time
from algorithms import ZAlgorithm
from helper_functions import expasy  # Funcion auxiliar para traducir secuencias geneticas

# Funcion que encuentra donde se produce la proteina dentro de las secciones del virus en el archivo de proteinas
def tarea3():
    genome = ""  # Variable para guardar la secuencia del genoma

    # Leemos el archivo del genoma SARS-COV-2, ignorando las lineas que comienzan con ">"
    with open("genomes/SARS-COV-2-MN908947.3.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genome += line

    # Traducimos la secuencia genetica a una secuencia de proteinas usando la funcion 'expasy'
    genomeProteinSequence = expasy.translate(genome)

    # Usamos el cronometro
    startTime = time.time()

    # Leemos el archivo de las secuencias de proteinas
    with open("seq-proteins.txt") as file:
        for line in file.read().splitlines():
            # Si la linea comienza con ">", es el nombre de una proteina
            if line[0] == ">":
                print("\nProteína:", line.replace(">", ""))  # Mostramos el nombre de la proteina
            else:
                # Buscamos la secuencia de aminoacidos en la secuencia de proteinas traducida con el algoritmo Z
                genomeIndices = ZAlgorithm.find(genomeProteinSequence, line)

                # Si la secuencia de aminoacidos fue encontrada
                if len(genomeIndices) > 0:
                    print("Indices en el genoma:", genomeIndices)  # Mostramos los indices donde se encontro la secuencia
                    # Mostramos los primeros 4 aminoacidos a partir del indice de la coincidencia
                    print("Secuencia de aminoácidos:", genomeProteinSequence[genomeIndices[0]:genomeIndices[0]+4])
                else:
                    print("No se encontró la secuencia de aminoácidos en el genoma")  # Si no se encuentra, mostramos este mensaje

    # Tiempo total de ejecucion
    print("\nTiempo de ejecución:", round((time.time() - startTime) * 1000, 2), "ms")
