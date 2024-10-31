class teste:
    def __init__(self):
        self.a=""
    def dados_usuario(self):
        usuarios = [
            {"usuario": "user1", "senha": "senha1", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user2", "senha": "senha2", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user3", "senha": "senha3", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user4", "senha": "senha4", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user5", "senha": "senha5", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user6", "senha": "senha6", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user7", "senha": "senha7", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user8", "senha": "senha8", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user9", "senha": "senha9", "saldo_crédito": 1000, "saldo_debito_pix": 2000},
            {"usuario": "user10", "senha": "senha10","saldo_crédito": 1000, "saldo_debito_pix": 2000}
        ]
        return usuarios
    
class produtos:
    def __init__(self):
        self.a=""
    def produtos_loja(self):
        produtos = [
            {"nome": "Notebook", "marca": "Dell", "valor": 3500.00},
            {"nome": "Smartphone", "marca": "Samsung", "valor": 2000.00},
            {"nome": "Fone de Ouvido", "marca": "Sony", "valor": 250.00},
            {"nome": "Teclado", "marca": "Logitech", "valor": 150.00},
            {"nome": "Monitor", "marca": "LG", "valor": 1200.00}
        ]
        return produtos