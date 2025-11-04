with open('roteiro.txt',"r",encoding="utf-8") as f:
    contador=0
    linhas=f.readlines()
    print("Primeiras 25 linhas:")
    for i in linhas:
        if contador >= 25:
            break
        print(i.rstrip())
        contador+=1
    print(f"Nº de linhas: {len(linhas)}")
    maior = max(linhas, key=len)
    print(f"Maior Linha:\n{maior}")
    f.seek(0)
    texto=f.read().lower()
    count_nonato=texto.count("nonato")
    cont_iria=texto.count("íria")
    print(f"Contagem nonato:{count_nonato} | Contagem íria: {cont_iria}")