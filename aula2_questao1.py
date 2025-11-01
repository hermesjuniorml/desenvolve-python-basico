data=str(input("Digite uma data de nascimento: "))
meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
dia=data.split('/')[0]
mes=int(data.split('/')[1])-1
ano=data.split('/')[2]
print(f"Você nasceu em {dia} de {meses[mes]} de {ano}.")