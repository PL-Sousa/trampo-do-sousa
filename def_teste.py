def perguntar_nome():
    nome = input ("qual o seu nome?")
    idade = int(input("qual a sua idade"))
    return nome, idade

nome1, idade1 = perguntar_nome()
print(f"seu nome é {nome1}")
print(f"Vc tem {idade1} anos")






