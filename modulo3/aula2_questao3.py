idade=int(input("Digite sua idade: "))
jogos_totais_str=input("Já jogou pelo menos 3 jogos de tabuleiro? ")
jogos_totais = False
jogos_vencidos=int(input("Quantos jogos já venceu? "))

if(jogos_totais_str == 'True'):
    jogos_totais = True
    
apto=((15 < idade < 19) and (jogos_totais) and (jogos_vencidos > 2))
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")