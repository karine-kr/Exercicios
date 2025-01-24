numero = int(input("Digite um valor entre 1 e 10: "))
aux = 1

while True: 
    if numero >= 1 and numero <= 10:
        if aux == 1:
            print("Tabuada do %d:" % numero)
        print("%d x %d = %d" % (aux, numero, (aux*numero)))
        aux += 1
        if aux > 10:
            break
    else:
        numero = int(input("Digite um valor válido entre 1 e 10: "))
        aux = 1