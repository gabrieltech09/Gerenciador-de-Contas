# ...existing code...
from contas_db import carregar_contas
import csv
import os
import sys
import subprocess

def exportar_csv(nome_arquivo='contas_exportadas.csv'):
    contas = carregar_contas()
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['sistema', 'usuario', 'senha'])
        for conta in contas:
            writer.writerow([conta.get('sistema', ''), conta.get('usuario', ''), conta.get('senha', '')])

    print(f"Contas exportadas para {nome_arquivo}")

    # tenta abrir o arquivo no aplicativo padrão
    try:
        caminho = os.path.abspath(nome_arquivo)
        if os.name == 'nt':  # Windows
            os.startfile(caminho)
        elif sys.platform == 'darwin':  # macOS
            subprocess.run(['open', caminho], check=False)
        else:  # Linux/other
            subprocess.run(['xdg-open', caminho], check=False)
    except Exception as e:
        print('Não foi possível abrir o arquivo automaticamente:', e)
# ...existing code...