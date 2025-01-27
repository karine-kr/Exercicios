aux = 1

while True:
    if aux >= 1: 
        nota1 = float(input("Digite a primeira nota: "))
        nota2  = float(input("Digite a segunda nota: "))
        notas = (nota1, nota2)
        somatorario = sum(notas) 
        media = somatorario / len(notas)
        if media >=7 :
            print('\n"Aprovado", a média final foi de {:.2f}'.format(media))
        else:
            print('\n"Reprovado", a média final foi de {:.2f}'.format(media))
        novoCalculo = input(('\nDeseja realizar um novo cálculo? Digite "s" para sim ou "n" para não\n\n'))
        if novoCalculo == "s":
            aux += 1
        else:
            break    
