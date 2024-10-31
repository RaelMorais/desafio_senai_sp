import aaaaa
while True:
    usuario = input("Entre com o usuário: ")
    senha = input("Entre com a sua senha: ")
    usuario_encontrado = False
    for u in aaaaa.teste().dados_usuario():
        if u["usuario"] == usuario and u["senha"] == senha:
            usuario_encontrado = True
            print(f"Seja bem vindo {usuario}")
            saldo = " ".join([str(float(u["saldo_debito_pix"]))])
            saldo_credito =" ".join([str(float(u["saldo_crédito"]))])
            print(f"Seu saldo no dédito é R${saldo}")
            print(f"Seu saldo no crédito é R${saldo_credito}")
    if not usuario_encontrado:
        print("Erro: Usuário ou senha inválidos.")
   
