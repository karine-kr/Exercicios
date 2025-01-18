nome = input("Digite o seu nome do produto: ")
preco  = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade de produto: "))

if quantidade <= 10:
    print('O preço total sem desconto, ficando no valor de R${:.2f}'.format(preco))
elif quantidade >= 11 and quantidade <= 20:
    novo = preco - (preco * 10 / 100)
    print('O preço está com 10% de desconto, ficando no valor de R${:.2f}'.format(novo))
elif quantidade >= 21 and quantidade <= 50:
    novo = preco - (preco * 20 / 100)
    print('O preço está com 20% de desconto, ficando no valor de R${:.2f}'.format(novo))
elif quantidade > 50:
    novo = preco - (preco * 25 / 100)
    print('O preço está com 25% de desconto, ficando no valor de R${:.2f}'.format(novo))