#DB de frases e entradas de dd

import sqlite3

from contextlib import closing

class Querys(object):
    def __init__(self,query=''):
        self.query=query
        self.myDatabase='Katia.db'

    def create(self,query=''):
        print(query)
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

    def verifcD(self,data='',frase=''):
        aux_inf=[]
        c = self.createConnection().cursor()
        with closing(c) as c:
            c.execute('select data,frases from says where data = "%s" and frases= "%s" '%(data,frase))
            result = c
            for x in result:
                aux_inf.append(x)
                if x == None:
                    break

        if len(aux_inf)>=1:
            return True
        else:
            return False
        
    def insertD(self,data='',frase=''):
        
        query='''insert into says (data,frases) values(?,?)'''
        retorn = self.verifcD(data,frase)
        if retorn:
            #print("pass!")
            pass
        else:
            #print("nao pass!")
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
    def updateRegister(self,query_update=''):
        #Criar logica disso aq
        #Exemplo query de update: update says frases = 'nova frase' where data = 'x.x.x'
        self.query=query_update

