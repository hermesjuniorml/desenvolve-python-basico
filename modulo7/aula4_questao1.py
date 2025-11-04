import os
frase = str(input("Digite uma frase: "))
with open('frase.txt',"w") as f:
    f.write(frase)
    print(f"Frase saalva em {os.path.abspath('frase.txt')}")