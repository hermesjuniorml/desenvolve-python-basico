def validador_senha(senha):
    if len(senha) < 8:
        return False
    tem_maiuscula=any(c.isupper() for c in senha)
    tem_minuscula=any(c.islower() for c in senha)
    tem_numero=any(c.isdigit() for c in senha)
    tem_especial=any(c in "@#$%&*!?_-+=" for c in senha)
    return all([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))