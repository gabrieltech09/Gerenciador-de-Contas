import os, time
from contas_db import adicionar_conta, carregar_contas, salvar_contas

def limpar_tela():
    os.system('cls')

def pausar(segundos):
    time.sleep(segundos)


# funcoes para o sistema de gerenciamento de contas
def cadastrar():
    print('Cadastrar conta')
    sistema = input('Digite o nome do sistema que deseja cadastrar: ')
    usuario = input('Digite o nome do usuário: ')
    senha = input('Digite a senha: ')
    adicionar_conta(sistema, usuario, senha)
    print('Conta cadastrada com sucesso!')
    pausar(2)
    limpar_tela()

def ver_contas():
    print('Exibindo contas...')
    contas = carregar_contas()
    for conta in contas:
        pausar(1)
        print(f"Sistema: {conta['sistema']}, Usuário: {conta['usuario']}, Senha: {conta['senha']}")
    input('Pressione Enter para continuar')
    limpar_tela()
    
def editar_conta():
    contas = carregar_contas()
    if not contas:
        print('Nenhuma conta cadastrada')
        pausar(2)
        limpar_tela()
        return

    print('Editar conta - Selecione a conta:')
    for i, conta in enumerate(contas, 1):
        print(f"[{i}] Sistema: {conta['sistema']}, Usuário: {conta['usuario']}, Senha: {conta['senha']}")

    escolha = input('Digite o número da conta que deseja editar ou o nome do sistema: ').strip()
    idx = None

    if escolha.isdigit():
        i = int(escolha) - 1
        if 0 <= i < len(contas):
            idx = i
    else:
        for i, conta in enumerate(contas):
            if conta['sistema'].lower() == escolha.lower():
                idx = i
                break

    if idx is None:
        print('Conta não encontrada.')
        pausar(2)
        limpar_tela()
        return

    conta = contas[idx]
    novo_sistema = input(f'Digite o novo nome do sistema (atual: {conta["sistema"]}): ') or conta['sistema']
    novo_usuario = input(f'Digite o novo nome do usuário (atual: {conta["usuario"]}): ') or conta['usuario']
    nova_senha = input(f'Digite a nova senha (atual: {conta["senha"]}): ') or conta['senha']

    conta['sistema'] = novo_sistema
    conta['usuario'] = novo_usuario
    conta['senha'] = nova_senha

    salvar_contas(contas)
    print('Conta editada com sucesso!')
    pausar(2)
    limpar_tela()
    
    
    
    
    
    
    
    
    
    '''print('Editar conta')
    input('Digite o nome do sistema que deseja editar: ')
    input('Digite o novo nome do usuário: ')
    input('Digite a nova senha: ')
    print('Conta editada com sucesso!')
    pausar(2)
    limpar_tela()'''

def deletar_conta():
    contas = carregar_contas()
    if not contas:
        print('Nenhuma conta cadastrada.')
        pausar(2)
        limpar_tela()
        return

    print('Deletar conta - selecione a conta:')
    for i, conta in enumerate(contas, 1):
        print(f"[{i}] Sistema: {conta['sistema']}, Usuário: {conta['usuario']}")

    escolha = input('Digite o número da conta ou o nome do sistema: ').strip()
    idx = None

    if escolha.isdigit():
        i = int(escolha) - 1
        if 0 <= i < len(contas):
            idx = i
    else:
        for i, conta in enumerate(contas):
            if conta['sistema'].lower() == escolha.lower() or escolha.lower() in conta['sistema'].lower():
                idx = i
                break

    if idx is None:
        print('Conta não encontrada.')
        pausar(2)
        limpar_tela()
        return

    conta = contas[idx]
    confirm = input(f"Confirma exclusão da conta '{conta['sistema']}' (usuário: {conta['usuario']})? (s/N): ").strip().lower()
    if confirm != 's':
        print('Exclusão cancelada.')
        pausar(2)
        limpar_tela()
        return

    contas.pop(idx)
    salvar_contas(contas)
    print('Conta deletada com sucesso!')
    pausar(2)
    limpar_tela()

def deletar_todas_contas():
    contas = carregar_contas()
    if not contas:
        print('Nenhuma conta cadastrada.')
        pausar(2)
        limpar_tela()
        return

    print(f'Atenção: {len(contas)} contas serão apagadas.')
    confirm = input("Digite 'DELETAR' (tudo maiúsculo) para confirmar a exclusão de todas as contas: ").strip()
    if confirm != 'DELETAR':
        print('Exclusão em massa cancelada.')
        pausar(2)
        limpar_tela()
        return

    salvar_contas([])
    print('Todas as contas foram deletadas.')
    pausar(2)
    limpar_tela()

def exportar_conta():
    from exportar import exportar_csv
    exportar_csv()
    pausar(2)
    limpar_tela()

def sair_sistema():
    print('Saindo do sistema...')
    pausar(2)
    limpar_tela()
    print('Sistema encerrado. Até mais!')



    



    