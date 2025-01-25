aux = 1

while True:
    if aux <= 3: 
        usuario = (input("Digite o usuário: "))
        senha  = (input("Digite a senha: "))
        if usuario == 'aluno' and senha == 'segredo':
            print ('\nBem vindo!!!!!\n')
            break
        else:
            print('\nLogin não efetuado! Digite novamente os dados.\n')
            aux += 1
    else:
        print('\nUsuário Bloqueado!!!!\n')
        break