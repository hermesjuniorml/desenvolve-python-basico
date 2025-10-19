from datetime import datetime

data_e_hora = datetime.now()
data_texto = data_e_hora.strftime("%d/%m/%Y")
hora_texto = data_e_hora.strftime("%H:%m")
print(f"Data: {data_texto}")
print(f"Hora: {hora_texto}")