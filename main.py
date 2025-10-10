from funcoes import limpar_tela, pausar
from funcoes import cadastrar, ver_contas, editar_conta, deletar_conta, exportar_conta, sair_sistema


main = True
while main:
    limpar_tela()
    print('=== Sistema de Gerenciamento de Contas ===')
    print('----------------------------------------------')
    print('''\n
    [1] - Cadastrar conta
    [2] - Ver contas
    [3] - Editar conta
    [4] - Deletar conta
    [5] - Exportar contas
    [6] - Sair do sistema
    ''')
    opcao = input('Escolha uma das opções acima: ')
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        ver_contas()
    elif opcao == '3':
        editar_conta()
    elif opcao == '4':
        deletar_conta()
    elif opcao == '5':
        exportar_conta()
    elif opcao == '6':
        sair_sistema()
        main = False
    else:
        print('Opção inválida! Tente novamente.')
        pausar(2)
        limpar_tela()
  
   

    
