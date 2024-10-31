import aaaaa

def menu():
    usario_produto = input("Qual produto deseja comprar? ")
    valor_produto = float(input("Qual valor do produto "))
    escolha = input("Escolha abaixo \n1-Pix \n2-Dinheiro \n3-Débito \n4-Crédito \n").strip().lower()
    
    match escolha:
        case "pix":
                saldo = " ".join([str(float(["saldo_debito_pix"]))])
                valor = valor_produto - saldo
                print(valor)
        case "dinheiro":
            print("Olá mundo")
        case "débito":
            print("Olá mundo")
        case "crédito":
            print("Olá mundo")
menu()