genero=input("Por favor insira seu gênero: ")
idade=int(input("Insira sua idade: "))
tempo_servico=int(input("Insira o tempo de trabalho: "))
# tecnicamente ter mais de 60 anos é ter 61... se estivesse completado 60 anos seria outra situação
aposentavel=((genero=="F" and idade > 60) or (genero=="M" and idade > 65)) or (tempo_servico >=30) or (idade >= 60 and tempo_servico >=25)
print("Possibilidade da aposentadoria: ", aposentavel)