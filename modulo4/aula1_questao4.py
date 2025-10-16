n=int(input("Insira o valor de n: "))
maior=0
while (n > 0):
    x=int(input("Insira o valor de x: "))
    if(x>maior):
        maior=x
    n-=1
print(f"maior é: {maior}")
    
