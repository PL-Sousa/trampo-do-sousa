historico_transacoes = []

saldo = 0

while True:
    valor = int(input("insira um valor"))

    saldo += valor

    registro = "voce depositou" + str(saldo)

    historico_transacoes.append(registro)
    registro2 = "voce depositou" + str(saldo)

    historico_transacoes.append(registro2)

    break

print(historico_transacoes)

#for transacoes in historico_transacoes:
   # print("->" + registro)

