n1=int(input("Insira a primeira nota: "))
n2=int(input("Insira a segunda nota: "))
n3=int(input("Insira a terceira nota: "))
m=(n1+n2+n3)/3

if (m>=60):
    print("Aprovado!")
elif(m>=40):
    print("Recuperação!")
else:
    print("Reprovado!")
print("Fim")