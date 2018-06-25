                        #Nucleotidic count

#!/home/cw/Dropbox/Scripts/DNAc
#C:\Users\jp\Documents\GitHub\DNA\DNAc.py
#C:\Users\jp\Documents\GitHub\DNA\rna.txt
#TEST: !/home/cw/Dropbox/Scripts/OI.TXT

print("""
             _____  _   _             _______          __
            |  __ \| \ | |   /\      / ____\ \        / /
            | |  | |  \| |  /  \    | |     \ \  /\  / /
            | |  | | . ` | / /\ \   | |      \ \/  \/ /
            | |__| | |\  |/ ____ \  | |____   \  /\  /
            |_____/|_| \_/_/    \_\  \_____|   \/  \/


            welcome to DNA CW
            Chose One item:
                    0 = DNA count
                    1 = mRNA
                    2 = DNA Translate """)
###############################################################################

L = input("wich letter:");
if L == "0":
    F = input("Coloque o diretorio do arquivo aqui:")
    FC = len(F) # Conta a string F
    if (FC > 1):
        f = open (F) # estabeleci que f= a um diretorio
        DNA = f.read(); # estabeleci que DNA = a leitura de f
        A = DNA.count('A'); #count Ã© utilizado para contar um termo no arquivo
        T = DNA.count('T'); # estabeleci que cada base possui sua varaivel
        C = DNA.count('C');
        G = DNA.count('G');
        print ("A = ", A, "\nT = ", T, "\nC = ", C, "\nG = ", G)
    else:
        print("NO DIRECTORE TRY AGAIN")
###############################################################################
elif L == "1":
    F = input("Coloque o diretorio do arquivo aqui:")
    FC = len(F) # Conta a string F
    if (FC > 1):
        f = open (F)
        RNA = f.read()
        RNA1 = RNA.replace('T', 'U')
        print (RNA1)
###############################################################################
elif L == "2":
    rna = input("Coloque o diretorio do arquivo aqui:")
    r = ()
    f = {'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
         'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
         'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
         'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
         'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
         'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
         'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
         'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
         'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
         'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
         'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
         'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
         'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
         'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
         'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
         'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}
    r = ()
    for line in f:
        line = line.strip()
        line =  [(r.split(' ')[0], r.split(' ')[1]) for codon in r.split(r'[ ]{2,3}', line) if codon]
        for r in line:
            table[r[0]] = r[1]
     # estabeleci que f= a um diretorio



    def translatio(rna):
        protein = ''
        for start in range(0, len(rna), 3):
            if table[rna[start: start+3]] !='stop':
                protein +=table[rna[start+3]]
            return protein

else:
    print("Error. CHOSE ONE ITEM!!!")
