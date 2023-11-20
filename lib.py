from mysql.connector import (connection)



db_conexao = connection.MySQLConnection(host='localhost',
                                        user='root',
                                        password='',
                                        database='CURRICULO')

    



class Candidato():
  
    def cadastrar(nome, telefone, minibio, entrevista, teste_pratico, teste_teorico, avaliacao_softskill):
        cursor = db_conexao.cursor()
        cursor.execute(f"INSERT INTO candidato (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skill) VALUES ('{nome}', {telefone}, '{minibio}', {entrevista}, {teste_pratico}, {teste_teorico}, {avaliacao_softskill})")
        db_conexao.commit()
        db_conexao.close()

    def listar(listagem):
        cursor = db_conexao.cursor()
        cursor.execute("SELECT * FROM candidato")
        listagem = cursor.fetchall()
        db_conexao.close()
        return listagem
    
    def filtrar(entrevista, teste_pratico, teste_teorico, avaliacao_softskill):
        cursor = db_conexao.cursor()
        cursor.execute(f"SELECT * FROM candidato WHERE entrevista >= {entrevista} AND teste_teorico >= {teste_teorico} AND teste_pratico >= {teste_pratico} AND softskill >= {avaliacao_softskill}")
        cursor.fetchall()
        db_conexao.close()   

