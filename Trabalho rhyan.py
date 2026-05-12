print("===== JOVEM FINANCEIRO =====")

opcao = input("""
1 - Registrar ganhos
2 - Registrar gastos
3 - Ver saldo
Escolha uma opção: 
""")

if opcao == "1":
    ganho = float(input("Digite o valor do ganho: "))
    print("Ganho registrado:", ganho)

elif opcao == "2":
    gasto = float(input("Digite o valor do gasto: "))
    print("Gasto registrado:", gasto)

elif opcao == "3":
    saldo = 100
    print("Seu saldo é:", saldo)

else:
    print("Opção inválida")

print("\nPrograma finalizado.")