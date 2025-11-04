import os
file=open("frase.txt", "r", encoding="utf-8").read().replace(" ", "\n")

with open("palavras.txt", 'w', encoding="utf-8") as palav:
    palav.write(file)
    print(file)