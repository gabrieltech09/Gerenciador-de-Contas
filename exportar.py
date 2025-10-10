from contas_db import carregar_contas

def exportar_csv(nome_arquivo='contas_exportadas.csv'):
    contas = carregar_contas()
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write('sistema,usuario,senha\n')
        for conta in contas:
            f.write(f"{conta['sistema']},{conta['usuario']},{conta['senha']}\n")
    print(f"Contas exportadas para {nome_arquivo}")