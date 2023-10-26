import sqlite3

def gerar_id():
    # Conexão com db
    connection = sqlite3.connect('Projeto_Koru_02.db')
    cursor = connection.cursor()

    # Busca o último id registrado no db
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='Membros'")
    next_id = cursor.fetchone()[0]

    # Retorna o id com incremento
    return next_id + 1

def criar_membro(nome, descricao, foto):
    try:
        connection = sqlite3.connect('Projeto_Koru_02.db')
        cursor = connection.cursor()

        sql_insert = "INSERT INTO Membros(nome, descricao, foto) VALUES(?, ?, ?)"
        cursor.execute(sql_insert, (nome, descricao, foto))

        membro_id = cursor.lastrowid
        connection.commit()
        connection.close()
        return membro_id

    except Exception as ex:
        print(ex)
        return 0  

def retornar_membros():
    try:
        # Conexão com db
        connection = sqlite3.connect('Projeto_Koru_02.db')
        cursor = connection.cursor()

        #Lista todos os membros do banco de dados
        sql_select_varios = "SELECT * FROM Membros"
        cursor.execute(sql_select_varios)
        lista_membros = cursor.fetchall()

        # Fecha conexão com db e retorna todos os membros
        connection.close()
        return lista_membros

    except Exception as ex:
        return False

def retornar_membro(id: int):
    try:
        # Verifica se o usuário deseja criar um novo membro
        # Retorna um novo id e os campos nome, descricao e foto em branco
        if id == 0:
            return gerar_id(), "", "", ""
        
        # Caso o usuário não deseje criar um novo membro, então cria conexão com db
        connection = sqlite3.connect('Projeto_Koru_02.db')
        cursor = connection.cursor()

        #Lista um membro do banco de dados
        sql_select_unico = "SELECT * FROM Membros WHERE id_membro=?"
        cursor.execute(sql_select_unico, (id, ))
        id, nome, descricao, foto = cursor.fetchone()

        # Fecha conexão com db e retorna os dados obtidos do usuário buscado
        connection.close()
        return id, nome, descricao, foto 

    except:
        return False
    
def atualizar_membro(id: int, nome, descricao, foto):
    try:
        # Abre conexão com banco de dados
        connection = sqlite3.connect('Projeto_Koru_02.db')
        cursor = connection.cursor()

        # Executa SQL para atualizar dados de um membro
        sql_update = "UPDATE Membros SET nome = ?, descricao = ?, foto = ? WHERE id_membro = ?"
        cursor.execute(sql_update, (nome, descricao, foto, id))

        # Realiza commit no banco de dados e fecha conexão
        connection.commit()
        connection.close()
        return True
    
    except Exception as ex:
        print(ex)
        return False

def remover_membro(id: int):
    try:
        connection = sqlite3.connect('Projeto_Koru_02.db')
        cursor = connection.cursor()

        sql_delete = "DELETE FROM Membros WHERE id_membro = ?"
        cursor.execute(sql_delete, (id, ))

        connection.commit()
        connection.close()
        return True
    
    except Exception as ex:
        print(ex)
        return False


"""" TESTE DE VALIDAÇÃO DA CONEXÃO COM BANCO DE DADOS

nome = "Magno Dyego"
descricao = "Lipsum lorem"
foto = "<caminho_foto>"

id = criar_membro(nome, descricao, foto)
print(id)
print(retornar_membro(id))

id, nome, descricao, foto = retornar_membro(id)
atualizar_membro(id, "Dyego Magno", descricao, foto)

print(retornar_membros())

remover_membro(id)

print(retornar_membros())
"""
