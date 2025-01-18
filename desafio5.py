nome = (input('Digite o nome do vendedor: '))
valor  = float(input('Digite o valor do imóvel R$: '))


if valor < 30000.00:
    comissao = valor * 10 / 100
    novo = valor + (valor * 10 / 100)
    print(f"\n{nome}, o valor sem comissão do imóvel é RS {valor:.2f}, \n O valor de 10% da comissão é de R$ {comissao:.2f},\n Ficando um valor total do imóvel de {novo:.2f}".format(valor,comissao,novo))
elif valor >= 30000.00 and valor < 50000.00:
    comissao = valor * 15 / 100
    novo = valor + (valor * 15 / 100)
    print(f"\n{nome}, o valor sem comissão do imóvel é RS {valor:.2f}, \n O valor de 15% da comissão é de R$ {comissao:.2f}, \n Ficando um valor total do imóvel de {novo:.2f}".format(valor,comissao,novo))
elif valor >= 50000.00:
    comissao = valor * 20 / 100
    novo = valor + (valor * 20 / 100)
    print(f"\n{nome}, o valor sem comissão do imóvel é RS {valor:.2f}, \n O valor de 20% da comissã3o é de R$ {comissao:.2f}, \n Ficando um valor total do imóvel de {novo:.2f}".format(valor,comissao,novo))