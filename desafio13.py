nomes = []
nomes2 = []

for mensagem in range (10):
    mensagem = input('\nDigite o nome do aluno: ')
    nomes.append(mensagem)

novonumero = input('\nDigite o nome do aluno que deseja procurar: ')
nomes2.append(novonumero)
if novonumero in nomes:
    print('\nAchei\n')

else: 
    print('\nNão achei\n')