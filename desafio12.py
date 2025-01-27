vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
vetor2 = []

for valor in vetor1:
    if valor % 2 != 0:
        vetor2.append(valor)
        quantidade = len(vetor2)
print(f'\nA quantidade de números impares é {quantidade}, sendo os números:{vetor2}\n')