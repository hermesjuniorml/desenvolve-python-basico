n=int(input())
sapos=0
ratos=0
coelhos=0
while(n>0):
    qtd, animal = map(str, input().split(" "))
    if(animal=="C"):
        coelhos+=int(qtd)
    elif(animal=="S"):
        sapos+=int(qtd)
    elif(animal=="R"):
        ratos+=int(qtd)
    else:
        print("Erro na entrada do usuário... Saindo do programa.")
        break
    n-=1
total=sapos+ratos+coelhos
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos/total*100:.2f} %")
print(f"Percentual de ratos: {ratos/total*100:.2f} %")
print(f"Percentual de sapos: {sapos/total*100:.2f} %")