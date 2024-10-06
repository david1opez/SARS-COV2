import time
from algorithms import Manacher

# Funcion que busca los palindromos mas largos en las tres secuencias geneticas
def tarea2():
    executionTime = 0.0  # Variable para guardar el tiempo de ejecucion
    genM, genORF1AB, genS = "", "", ""  # Variables para guardar las secuencias de los genes

    # En esta seccion leemos y guardamos el contenido de los archivos ignorando las lineas que comienzan con ">"
    # Archivo 'gen-M.txt'
    with open("genes/gen-M.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genM += line
        
    # Archivo 'gen-ORF1AB.txt'
    with open("genes/gen-ORF1AB.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genORF1AB += line
    
    # Archivo 'gen-S.txt'
    with open("genes/gen-S.txt") as file:
        for line in file.read().splitlines():
            if line[0] != ">":
                genS += line
    
    # Usamos el cronometro
    startTime = time.time()

    # Usamos el algoritmo Manacher para encontrar el palindromo mas largo en cada secuencia genetica
    genMPalindrome = Manacher.longestPalindrome(genM)
    genORF1ABPalindrome = Manacher.longestPalindrome(genORF1AB)
    genSPalindrome = Manacher.longestPalindrome(genS)

    # Calculamos el tiempo de ejecucion
    executionTime = time.time() - startTime

    # Mostramos la longitud del palindromo mas largo de cada secuencia
    print("Gen M:")
    print("Longitud del palíndromo más largo:", len(genMPalindrome))
    
    print("\nGen ORF1AB:")
    print("Longitud del palíndromo más largo:", len(genORF1ABPalindrome))

    print("\nGen S:")
    print("Longitud del palíndromo más largo:", len(genSPalindrome))

    # Guardarmos estos palindromos en un archivo de texto
    with open("tarea2.txt", "w") as file:
        file.write("Gen M longest palindrome:\n")
        file.write(genMPalindrome)

        file.write("\n\nGen ORF1AB longest palindrome:\n")
        file.write(genORF1ABPalindrome)

        file.write("\n\nGen S longest palindrome:\n")
        file.write(genSPalindrome)
    
    # Tiempo total de ejecucion
    print("Tiempo de ejecución del algoritmo: ", round(executionTime*1000,1), "ms")
