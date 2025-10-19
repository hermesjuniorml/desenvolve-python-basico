import random

valor=random.randint(1,10)
palpite=999
while palpite!=valor:
    palpite=int(input("Adivinhe o número entre 1 e 10: "))
    if(palpite > valor):
        print("Muito alto, tente novamente!")
    elif(palpite == valor):
        print(f"Correto! o número é {valor}!")
    else:
        print(f"Muito baixo, tente novamente!")