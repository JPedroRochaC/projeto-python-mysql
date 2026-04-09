nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))

if nome == "":
    print("Produto não cadastrado.")
elif preco <= 0:
    print("Preço inválido.")
elif quantidade == 0:
    print(f"O produto {nome} está sem estoque.")
else:
    valor_total = preco * quantidade
    print("\n--- PRODUTO CADASTRADO ---")
    print(f"Nome: {nome}")
    print(f"Preço: R$ {preco}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor total em estoque: R$ {valor_total}")

