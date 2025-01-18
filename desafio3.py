nota1 = float(input("Digite a primeira nota: "))
nota2  = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = (nota1, nota2, nota3)
somatorario = sum(notas) 
media = somatorario / len(notas)

if media < 5:
    print('"Reprovado", a nota foi de {:.2f}'.format(media))
elif media >= 5 and media < 7:
    print('"Recuperação", a nota foi de {:.2f}'.format(media))
else:
    print('"Aprovado", a nota foi de {:.2f}'.format(media))