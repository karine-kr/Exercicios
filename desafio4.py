numero1 = float(input('Digite o primeiro número: '))
numero2  = float(input('Digite o segundo número: '))
operacao = (input('Qual operação deseja fazer, digitando um dos seguintes operadores:  + , - , / * '))


match operacao:
    case '+':
        soma = (numero1, numero2)
        somatorario = sum(soma) 
        print('O valor foi de: {:.2f}'.format(somatorario))
    case '/':
        dividir = (numero1/numero2)
        print('O valor foi de: {:.2f}'.format(dividir))
    case '-':
        subtrair = (numero1-numero2)
        print('O valor foi de: {:.2f}'.format(subtrair))
    case '*':
        multiplicar = (numero1*numero2)
        print('O valor foi de: {:.2f}'.format(multiplicar))







