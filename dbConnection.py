import sqlite3

connection = sqlite3.connect('Projeto_Koru_02.db')
cursor = connection.cursor()

#Dados de teste
""""
nome = "Lucian Andrade"
descricao = "Lorem lipsum dolor sit amet"
foto = "<caminho_da_foto>"


#CREAT
sql_insert = "INSERT INTO Membros(nome, descricao, foto) VALUES(?, ?, ?)"
cursor.execute(sql_insert, (nome, descricao, foto))
"""

""""
#READ
#Lista todos os membros do banco de dados
sql_select_varios = "SELECT * FROM Membros"
cursor.execute(sql_select_varios)
lista_membros = cursor.fetchall()
for item in lista_membros:
    id, nome, descricao, foto = item
    print(f"{id} -> {nome}")
"""

""""
#Lista um membro do banco de dados
sql_select_unico = "SELECT id_membro, nome FROM Membros WHERE id_membro=?"
cursor.execute(sql_select_unico, (2, ))
id, nome = cursor.fetchone()
print(f"{id} -> {nome}")
"""

""""
#UPDATE
sql_update = "UPDATE Membros SET nome = ? WHERE id_membro = ?"
cursor.execute(sql_update, ("Mateus Porfirio", 2))
"""

sql_delete = "DELETE FROM Membros WHERE id_membro = ?"
cursor.execute(sql_delete, (2, ))

connection.commit()