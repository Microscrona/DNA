                        #Nucleotidic count

#!/home/cw/Dropbox/Scripts/DNAc
#TEST: !/home/cw/Dropbox/Scripts/OI.TXT

print (" _____  _   _             _______          __ \n|  __ \| \ | |   /\      / ____\ \        / / \n| |  | |  \| |  /  \    | |     \ \  /\  / /  \n| |  | | . ` | / /\ \   | |      \ \/  \/ /   \n| |__| | |\  |/ ____ \  | |____   \  /\  /    \n|_____/|_| \_/_/    \_\  \_____|   \/  \/")

print       ("\n welcome to DNA CW\n Chose One item:",
                "\n0 = DNA count",
                "\n1 = mRNA",
                "\n2 = DNA Transalate",);
################################################################################
L = int(input("wich letter:"));
if (L == 0):
    F = input("Coloque o diretorio do arquivo aqui:")
    FC = len(F) # Conta a string F
    if (FC > 2):
        f = open (F) # estabeleci que f= a um diretorio
        DNA = f.read(); # estabeleci que DNA = a leitura de f
        A = DNA.count('A'); #count Ã© utilizado para contar um termo no arquivo
        T = DNA.count('T'); # estabeleci que cada base possui sua varaivel
        C = DNA.count('C');
        G = DNA.count('G');
        print ("A = ", A, "\nT = ", T, "\nC = ", C, "\nG = ", G)
    else:
        print("NO DIRECTORE TRY AGAIN")
elif (L == 1):
    print("Wait update")
elif (L == 2):
    print("Wait update")
else:
    print("Error. CHOSE ONE ITEM!!!")
