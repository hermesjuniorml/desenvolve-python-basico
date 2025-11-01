# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
# Digite o número: 97651234
# Número completo: 99765-1234
# Digite o número: 980876543
# Número completo: 98087-6543 
num=' '
while num !='0':
    num=str(input("Digite o número: "))
    if  (7 < len(num) < 9):
        print(f"Número completo: 9{num[0:4]}-{num[4:8]}")
    elif (len(num)== 9)  and ( num[0]=='9'):
        print(f"Número completo: {num[0:5]}-{num[5:9]}")
    elif num=='0':
        break
    else:
        print("Insira um número com 8 dígitos ou com 9, para sair digite: 0")
