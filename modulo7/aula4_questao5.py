import os
livros = [
    ["O jogador", "Fiódor Dostoiévski", "1867", "352"],
    ["A fisioterapeuta e o dono do morro cadeirante", "Bruna Mattos", "2021", "198"],
    ["Misto Quente", "Charles Bukowski", "1982", "320"],
    ["Memórias Póstumas de Brás Cubas", "Machado de Assis", "1881", "160"],
    ["As Veias Abertas da América Latina", "Eduardo Galeano", "1971", "304"],
    ["Assim Falou Zaratustra", "Friedrich Nietzsche", "1883", "256"],
    ["História da Loucura", "Michel Foucault", "1961", "392"],
    ["Indústria Cultural e Sociedade", "Theodor W. Adorno", "1944", "180"],
    ["O Hobbit", "J. R. R. Tolkien", "1937", "310"],
    ["Maluquinho pelo Mundo", "Ziraldo Alves Pinto", "1983", "96"]
]
with open("meus livros.csv", "+a", encoding="utf-8") as csv:
    csv.writelines("Título,Autor,Ano de publicação,Número de páginas\n")
    # csv.writelines("O jogador,Fiodor Dostoiévski, 1867,232\n")
    for linha in livros:
        for item in linha:
            csv.writelines(item+("," if linha.index(item) != len(linha)-1 else ""))
        csv.writelines("\n")