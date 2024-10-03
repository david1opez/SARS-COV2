from tareas import tarea1, tarea2, tarea3, tarea4

def main():
    print("\n=========================================")
    print("                  TAREA 1                  ")
    print("=========================================\n")
    tarea1.tarea1("KMP") # "KMP" (32.63 ms avg.) or "BoyerMoore" (16.06 ms avg.)
    print("\n=========================================")
    print("                  TAREA 2                  ")
    print("=========================================\n")
    tarea2.tarea2() # Manacher (37.64 ms avg.)
    print("\n=========================================")
    print("                  TAREA 3                  ")
    print("=========================================\n")
    tarea3.tarea3() # ZAlgorithm (47.54 ms avg.)
    print("\n=========================================")
    print("                  TAREA 4                  ")
    print("=========================================\n")
    tarea4.tarea4()

if __name__ == "__main__":
    main()