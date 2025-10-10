import json
import os

ARQUIVO = 'contas.json'

def carregar_contas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

    
def salvar_contas(contas):
    with open(ARQUIVO, "w", encoding='utf-8') as f:
        json.dump(contas, f, indent=4)

def adicionar_conta(sistema, usuario, senha):
    contas = carregar_contas()
    contas.append({"sistema": sistema, "usuario": usuario, "senha": senha})
    salvar_contas(contas)

