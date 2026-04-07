produto = input('Digite seu produto: ')
preco = float(input('Digite o preço: '))
quant = int(input('Digite a quantidade: '))

if produto.strip() == "":
    print('PRODUTO não pode ficar vazio')
elif preco <= 0:
    print('PREÇO não pode ser 0')
elif quant <= 0:
    print('QUANTIDADE não pode ser 0')
else:
    vt = preco * quant
    print('---- Produto Cadastrado com Sucesso ----')
    print(f'Seu produto é: {produto}')
    print(f'Preço: R$ {preco:.2f}')
    print(f'Quantidade: {quant}')
    print(f'Valor total: R$ {vt:.2f}')



