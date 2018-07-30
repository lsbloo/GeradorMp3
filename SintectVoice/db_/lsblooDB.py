#DB de frases e entradas de dd

import sqlite3

class Querys(object):
    def __init__(self,query=''):
        self.query=query
        self.myDatabase='MerynDB'

    def createTables(self,query=''):
        self.query=query
        self.createConnection()
        cursor = conexao.cursor()
        cursor.execute(self.query)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("tabela criada !")
        
    def createConnection(self):
        global conexao
        conexao = sqlite3.connect(self.myDatabase)
        return conexao

    def insertD(self,data='',frase=''):
        query='''insert into says (data,frases) values(?,?)'''
        self.createConnection()
        cursor=conexao.cursor()
        dados=[(data,frase)]
        cursor.executemany(query,dados)
        
        conexao.commit()
        cursor.close()
        conexao.close()

    def resultset(self):
        query = ''' select * from says '''
        self.createConnection()
        cursor=conexao.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        vetor=[]
        for saidas in result:
            #print("Data: %s \n Frase %s "%(saidas))
            vetor.append(saidas)

    
        conexao.commit()
        cursor.close()
        conexao.close()
        return vetor

