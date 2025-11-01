frase=str(input("Digite uma frase: ")).lower()
obj=list(str(input("Digite a palavra objetivo: ")).lower())

palavras=frase.split(" ")
anagramas=[]
for palavra in palavras:
    total = 0
    for letra in palavra:
       if letra in obj:
           total+=1
    if total==4:
        anagramas.append(palavra)
        total=0       

print(f"Anagramas: {anagramas}")