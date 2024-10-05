import time
from algorithms import Manacher

def tarea2():
    executionTime = 0.0
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
    
    startTime = time.time()
    genMPalindrome = Manacher.longestPalindrome(genM)
    genORF1ABPalindrome = Manacher.longestPalindrome(genORF1AB)
    genSPalindrome = Manacher.longestPalindrome(genS)
    executionTime = time.time() - startTime

    print("Gen M:")
    print("Longitud del palíndromo más largo:", len(genMPalindrome))
    
    print("\nGen ORF1AB:")
    print("Longitud del palíndromo más largo:", len(genORF1ABPalindrome))

    print("\nGen S:")
    print("Longitud del palíndromo más largo:", len(genSPalindrome))

    with open("tarea2.txt", "w") as file:
        file.write("Gen M longest palindrome:\n")
        file.write(genMPalindrome)

        file.write("\n\nGen ORF1AB longest palindrome:\n")
        file.write(genORF1ABPalindrome)

        file.write("\n\nGen S longest palindrome:\n")
        file.write(genSPalindrome)
    
    print("Tiempo de ejecución del algoritmo: ", round(executionTime*1000,1), "ms")

