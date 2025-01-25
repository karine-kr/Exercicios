nomes = []
nomes2 = []

for mensagem in range (10):
    mensagem = input('digite o nome do aluno: ')
    nomes.append(mensagem)

novonumero = input('digite o nome do aluno que deseja procurar: ')
nomes2.append(novonumero)
if novonumero in nomes:
    print('\nAchei\n')
        # break
else: 
    print('\nNão achei\n')