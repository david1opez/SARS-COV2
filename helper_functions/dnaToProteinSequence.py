# Tabla de codones que mapea tripletes de ADN a aminoacidos
# Por cada triplete se asigna un aminoácido que es representado con una letra
# Un * indica un codon de parada
codon_table = {
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G'
}

# Funcion que traduce una secuencia de ADN a secuencia de proteinas
def translate(dna_sequence):
    # Inicializamos una lista vacia donde se almacena la secuencia de proteinas
    protein_sequence = []
    
    # Como cada codon tiene 3 bases, iteramos la secuencia de ADN en pasos de 3
    for i in range(0, len(dna_sequence), 3):
        # Extraemos un codon de tres letras.
        codon = dna_sequence[i:i+3]
        
        # Si el codon se encuentra en la tabla, procedemos al siguiente paso
        if codon in codon_table:
            # Si el codon no es un codon de parada (*), añadimos el aminoacido adecuado a la secuencia de proteinas.
            if(codon_table[codon] != '*'):
                protein_sequence.append(codon_table[codon])
        else:
            # Si el codon no esta en la tabla, añadimos un '?' para indicar un codon desconocido.
            protein_sequence.append('?')
            
    # Devolvemos la secuencia de proteinas como una cadena de texto.
    return ''.join(protein_sequence)
