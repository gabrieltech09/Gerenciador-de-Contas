import json
import os
import sys

# se o app for executável (PyInstaller) use o diretório do exe, senão use o diretório do script
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARQUIVO = os.path.join(BASE_DIR, 'contas.json')

def carregar_contas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_contas(contas):
    # garante que a pasta exista (não necessário se for mesma pasta do exe)
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    with open(ARQUIVO, "w", encoding='utf-8') as f:
        json.dump(contas, f, indent=4)

def adicionar_conta(sistema, usuario, senha):
    contas = carregar_contas()
    contas.append({"sistema": sistema, "usuario": usuario, "senha": senha})
    salvar_contas(contas)
