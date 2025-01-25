numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número, lembrando que ele deve ser diferente de zero "))
aux = 1

while True: 
    if numero2 != 0:
        divisao = numero1 % numero2
        print('O valor do resultado da divisão = ', divisao)
        break
    else:
        numero2 = float(input("Número igual a zero. Por favor, digite um novo número: "))