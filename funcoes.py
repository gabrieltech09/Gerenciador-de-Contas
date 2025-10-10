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
    print('Ver contas')
    input('Digite o nome do sistema que deseja ver: ')
    pausar(1)
    limpar_tela()
    print('Exibindo contas...')
    contas = carregar_contas()
    for conta in contas:
        pausar(1)
        print(f"Sistema: {conta['sistema']}, Usuário: {conta['usuario']}, Senha: {conta['senha']}")
    input('Pressione Enter para continuar')
    limpar_tela()
    
def editar_conta():
    print('Editar conta')
    input('Digite o nome do sistema que deseja editar: ')
    input('Digite o novo nome do usuário: ')
    input('Digite a nova senha: ')
    print('Conta editada com sucesso!')
    pausar(2)
    limpar_tela()

def deletar_conta():
    print('Deletar conta')
    input('Digite o nome do sistema que deseja deletar: ')
    print('Conta deletada com sucesso!')
    pausar(2)
    limpar_tela()

def exportar_conta():
    print('Exportar contas')
    print('Exportando contas...')
    pausar(2)
    limpar_tela()

def sair_sistema():
    print('Saindo do sistema...')
    pausar(2)
    limpar_tela()
    print('Sistema encerrado. Até mais!')



    



    