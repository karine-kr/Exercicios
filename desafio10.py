aux = 1

while True:
    if aux >= 1: 
        nota1 = float(input("Digite a primeira nota: "))
        nota2  = float(input("Digite a segunda nota: "))
        notas = (nota1, nota2)
        somatorario = sum(notas) 
        media = somatorario / len(notas)
        if media >=7 :
            print('"Aprovado", a nota foi de {:.2f}'.format(media))
        else:
            print('"Reprovado", a nota foi de {:.2f}'.format(media))
        novoCalculo = input(("Deseja realizar um novo cálculo? S ou N\n\n"))
        if novoCalculo == "S":
            aux += 1
        else:
            break    
