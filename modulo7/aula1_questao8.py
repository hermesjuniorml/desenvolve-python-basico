texto=str(input("Digite seu CPF (XXX.XXX.XXX-XX): ")).replace('.','').replace('-','')
primeiros_digitos=texto[0:9]
soma_primeiros_digitos=0
contador=10

for i in range(9):
    if(contador>=2):
        soma_primeiros_digitos+=int(primeiros_digitos[i])*contador
        contador-=1
digito_verificador= 0 if soma_primeiros_digitos/11 < 2 else int(11-(soma_primeiros_digitos%11))


dez_primeiros_digitos=texto[0:10]
contador=11
soma_dez_primeiros=0
for i in range(10):
    if (contador >=2):
        soma_dez_primeiros+=int(dez_primeiros_digitos[i])*contador
        contador-=1
segundo_digito_verificador= 0 if soma_dez_primeiros/11 < 2 else int(11-(soma_dez_primeiros%11))
testado=primeiros_digitos+str(digito_verificador)+str(segundo_digito_verificador)

if(texto==testado):
    print("CPF VÁLIDO")
else:
    print("CPF INVALIDO")