import random
def imprime_enforcado(fase):
    with open("gabarito_enforcado.txt","r") as gab:
        linhas=gab.readlines()
        inicio=(fase*5)-5
        fim=fase*5
        for i in range(inicio,fim):
            print(linhas[i].rstrip())
palavras=""
with open("gabarito_forca.txt","r") as arq:
    palavras=arq.readlines()
    
palavra=palavras[random.randint(0,9)].rstrip()
linhas=["_"]*len(palavra)
print(palavra)
erros=0
letras=[]
print(" _"*len(palavra))
while erros <= 6:
    x=str(input("Digite uma letra: "))
    if(x in palavra):
        letras.append(x)
    else:
        imprime_enforcado(erros+1)
        erros+=1
    for i in palavra:
        print(f"{i if i in letras else "_"}", end=" ")
    print()
    if(erros>=6):
        print("VOCE PERDEU!")
        imprime_enforcado(erros+1)
        break
    if(set(letras)==set(palavra)):
        print("PARABÉNS DESCOBRIU A PALAVRA!")
        break