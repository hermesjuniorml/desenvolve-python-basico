filtradas=[]
with open("spotify-2023.csv","r",encoding="latin-1") as f:
    linhas=f.readlines()
    contador=0
    for linha in linhas:
        if linha.count('"') == 0:
            campos=linha.split(',')
            contador+=1
            if(contador>1):
                if(2022>=int(campos[3])>=2012):
                    filtradas.append([campos[0],campos[1],int(campos[3]),int(campos[8])])
ordenada=sorted(filtradas, key=lambda x:x[3], reverse=True)
lista_por_ano=[]
for ano in range(2012,2023):
    for lin in ordenada:
        if int(lin[2]) == ano:
            lista_por_ano.append(lin)
            break
[print(item) for item in lista_por_ano]