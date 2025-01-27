numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número, lembrando que ele deve ser diferente de zero "))
aux = 1

while True: 
    if numero2 != 0:
        quociente = numero1 / numero2
        resto = numero1 % numero2
        print('\nO resultado da divisão consiste em:\n\nResto igual a {:.0f} e quociente igual a {:.0f}\n'.format(resto,quociente))
        break
    else:
        numero2 = float(input("Número igual a zero. Por favor, digite um novo número: "))