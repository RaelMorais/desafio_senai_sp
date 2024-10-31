# CONSULTA PRODUTOS
import aaaaa
marca = None
categoria = None
valor = None

consulta = input("Selecione o produto: ")

for u in aaaaa.produtos().produtos_loja():
    if u["nome"] == consulta:
          marca = str(u["marca"])
          categoria = str(u["nome"])
          valor = float(u["valor"])
if marca and categoria and valor is not None:
    print(f"Marca: {marca}, Categoria: {categoria}, Valor: R${valor:.2f}")