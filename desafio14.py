nomes = []

for valor in range (20):
    nome = input('Digite o nome: ')
    nomes.append(nome)

for valor2 in nomes:
    if valor2 == nome:
        # nomes.remove(nome)
        nomes_sem_repeticao = list(set(nomes))
        print(f'Os nomes sem repetições são:', nomes_sem_repeticao) 
