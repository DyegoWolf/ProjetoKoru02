equipe = {
    1: {
        "nome": "Dyego Magno Oliveira Souza",
        "descricao": "Lorem lipsum dolor sit amet",
        "foto": "<url>"
    },
    4: {
        "nome": "Dyego Magno Oliveira Souza",
        "descricao": "Lorem lipsum dolor sit amet",
        "foto": "<url>"
    }
}

def gerar_id():
    id = len(equipe) + 1
    return id

def criar_membro(nome, descricao, foto):
    equipe[gerar_id()] = {
        "nome": nome,
        "descricao": descricao,
        "foto": foto
    }

def retornar_membros():
    return equipe

def retornar_membro(id: int):
    if(id in equipe.keys()):
        return equipe[id]
    else:
        return {}
    
def atualizar_membro(id: int, dados_membros: dict):
    equipe[id] = dados_membros

def remover_membro(id: int):
    del equipe[id]

#print(retornar_membros(1))

criar_membro("Débora Evéllyn", "Lorem lipsum", "<urll>")

print(retornar_membros())

atualizar_membro(2, {"nome": "Luciene", "descricao": "Lipsum lorem", "foto": "<link"})

print(retornar_membro(2))

remover_membro(2)

print(retornar_membro(2))