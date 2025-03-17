nomes = []

for valor in range (20):
    nome = input('\nDigite o nome: ')
    nomes.append(nome)

for valor2 in nomes:
    if valor2 == nome:
        nomes_sem_repeticao = list(set(nomes))
        
print(f'\nOs nomes sem repetições são:', nomes_sem_repeticao) 
