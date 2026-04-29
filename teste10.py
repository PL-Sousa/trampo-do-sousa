# Entrada de dados
nome = input("Qual é o nome do Herói? ")
while True:
    classe = input("Escolha sua classe: Guerreiro ou Mago? ").lower().strip()
    if classe in ["guerreiro", "mago"]:
        classe = classe.title()
        break
    print("Classe inválida! Digite 'Guerreiro' ou 'Mago'.")
print("Bem-vindo'", nome, "Ótimo", classe)

print(" " * 50)
print("." * 50)
print(" " * 50)

# NÍVEL 1: Limite de nível
nivel = int(input("Qual o nível do seu herói? "))
if nivel>=101:
    print("O nivel maximo é 100.")
    nivel=1
    print("O seu nivel é",nivel)
elif nivel<=99:
    print("O seu nivel é",nivel)

hp = nivel * 50
print("Seu Hp é", hp)
mana = nivel * 30
print("Sua mana é", mana)

print(" " * 50)
print("." * 50)
print(" " * 50)
# =========================
# NÍVEL 2: Treinamento (loop + time)
# =========================
import time
print("Treinando por 3 anos...")
for i in range(3):
    print(f"Ano {i+1}...")
    time.sleep(1)
print("Treinamento concluído!")

print(" " * 50)
print("." * 50)
print(" " * 50)

print("Após o seu treinamento Você encontrou 10 Bombas!")
print("como um bom",classe)
print("Voce tera que decidir o seu caminho")
1 or 2
print("1 - Passar pelo meio da floresta")
print("2 - Contornar a floresta")
caminho = int(input("escolha um caminho"))

if caminho == 1:
    print("Há um grande caminho pela frente, Você tera que atravessar a floresta para chegar a Cidade Real!")
    print("Você escuta alguma coisa")
    print("1 - Se você vai verificar")
    print("2 - Se você vai seguir o seu caminho")
    escutar = int(input("Qual a sua escolha?"))
    if escutar == 1:
        print("Você encontrou um vendedor de Porções")
        
    




    # NÍVEL 2 e 3: Loja
    ouro = 100.50
    valor_pocao = 12.30

    print("Você tem", ouro, "de ouro")
    print("Cada poção custa", valor_pocao)

    quantidade = int(input("Quantas poções quer comprar? "))
    print("Certeza que Você vai precisar de porção?")

    # NÍVEL 3: impedir número negativo
    if quantidade <= 0:
        print("Quantidade inválida! Compra cancelada.")
    else:
        gasto = quantidade * valor_pocao

        # NÍVEL 2: verificar se tem dinheiro
        if ouro >= gasto:
            ouro -= gasto
            print("Compra realizada!")
            print("Você gastou:", gasto)
            print("Seu ouro restante é:", ouro)
        else:
            print("Ouro insuficiente! Compra recusada.")

    print(" " * 50)
    print("." * 50)
    print(" " * 50)

    # NÍVEL 4: Combate final
    print("Um monstro apareceu!")
    print("1 - Atacar")
    print("2 - Magia")
    print("3 - Fugir")
    print("4 - Jogar Bomba")
    import random
    vidamonstro = 100
    seuhp = 50
    tentativas = 10
    bomba = 10


    while vidamonstro > 0 and seuhp > 0 and tentativas > 0:
        dado = random.randint(1, 20)
        acao = int(input("Escolha uma ação: "))

        if acao == 1:
            vidamonstro -= dado
            print(f"Você atacou e causou {dado} de dano")
            print(f"Vida do monstro: {vidamonstro}")
            tentativas -= 1

        elif acao == 2:
            if mana >= 7:
                mana -= 7
                if dado >= 10:
                    vidamonstro -= dado
                    print(f"Magia acertou! Dano: {dado}")
                else:
                    seuhp -= dado
                    print(f"Magia falhou! Você tomou {dado} de dano")
            else:
                print("Mana insuficiente!")
                continue

            print(f"HP: {seuhp} | Mana: {mana}")
            tentativas -= 1

        elif acao == 3:
            if dado == 20:
                print("Você fugiu com sucesso!")
                break
            else:
                seuhp -= dado
                print(f"Falhou ao fugir! Tomou {dado} de dano")
                print(f"Seu HP: {seuhp}")
                tentativas -= 1

        elif acao == 4:  # 💣 AQUI ESTÁ A BOMBA CORRETA
            if bomba > 0:
                dano = 25
                vidamonstro -= dano

                if vidamonstro < 0:
                    vidamonstro = 0

                bomba -= 1
                tentativas -= 1

                print("💣 BUM!")
                print(f"Você causou {dano} de dano")
                print(f"Vida do monstro: {vidamonstro}")
                print(f"Bombas restantes: {bomba}")
                
            else:
                print("Você não tem mais bombas!")
                continue

        else:
            print("Ação inválida!")
            continue

        print(f"Tentativas restantes: {tentativas}")
        
        # RESULTADO FINAL
    if vidamonstro <= 0:
        print("🎉 Você venceu o monstro!")
    elif seuhp <= 0:
        print("💀 Você morreu!")
    elif tentativas == 0:
        print("😴 Você ficou sem energia!")

elif caminho == 2:
    print()