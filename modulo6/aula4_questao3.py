horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = []

pagamentos=[min(hora, 40)*ganho_por_hora + max(0, hora-40)*hora_extra for hora in horas_trabalhadas]
print(pagamentos)