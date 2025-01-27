aux = 1

while True:
    if aux <= 3: 
        usuario = (input("Digite o usuário: "))
        senha  = (input("Digite a senha: "))
        if usuario == 'aluno' and senha == 'segredo':
            print ('\nBem vindo!!!!!\n')
            break
        else:
            print('\nLogin não efetuado!.\n')
            aux += 1
    else:
        print('Usuário Bloqueado!!!!\n')
        break