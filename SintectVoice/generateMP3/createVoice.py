#!/usr/bin/env python

#IMport ggts Google

from gtts import gTTS
# execute mp3 imports

# importando classes de subdiretorios
import sys
sys.path.append("../db_")
sys.path.append("generates")
from lsblooDB import Querys
## manipular arquivos e diretorios
import os
import os.path
import subprocess as s

# ARQUIVO DE CONFIG - PARA OS PATHS DO MP3 LOG
global DIR
leitura = 'r'
escrita = 'w'
configTXT='pathMP3.txt'


DIR= open(configTXT,escrita)

def criarArquivosMP3(frases_VETOR):
    #print(frases)
    '''
    Cria os arquivos MP3, com as frases armazenadas no katia.
    é necessario pegar o caminho relativo de outra forma pois o os.path.expanduser()
    so me retorna /home/osvaldoairon/arq.mp3;
    
    '''
    extensao='mp3'
    aux=''
    zin=''
    kin=''
    extensoes=[]
    for i in frases_VETOR:            
        criarArquivomp3 = gTTS(i,lang="pt")
        aux += i
        aux += '.'
        aux += extensao
        kin+="/home/osvaldoairon/Área de Trabalho/SintectVoice/generateMP3/generates/"
        kin+=aux
        verifc = os.path.isfile(kin)
        extensoes.append(kin)
        kin=''
        #print(aux)
        if verifc:
            aux=''
            #print("pass! arq!")
            pass
        else:
            zin += '/home/osvaldoairon/Área de Trabalho/SintectVoice/generateMP3/generates/'
            zin += aux
            criarArquivomp3.save(zin)
            #print(aux)
            extensoes.append(zin)
            aux=''
            zin=''

    return extensoes
    

def extrairFrasesDB(Query):
    '''
    Parametro Objeto do tipo Query 
    Cria comunicação entre a minha classe Query que realiza as consultas no Katia.
    depois povoa o vetor com os dados do katia.
    '''
    #a.create('''create table says (data text,frases text) ''')
    Query.insertD("01/08/2018","bom?")
    frases =[]
    Query.resultset()
    vetor = []
    vetor = Query.resultset()

    for i in vetor:
        frases.append(i[1])
        #print(i[1])
    return frases
def createArqVoice(arquivomp3Audio):
    '''
     Criar um arquivo txt que armazena o caminho do arquivo MP3. para a funcao KAtiaSAYS
    '''
    

    try:
        meuPlayer='mplayer'
        #print(extensoes[6])
        for i in arquivomp3Audio:
            DIR.write("%s\n"%(i))
        DIR.close()

    except IndexError:
        pass

def loadPatchTXT():
    """
    Carrega Arquivos do DIR
    """
    try:
        
        list_of_path=[]
        DIR= open(configTXT,leitura)
        for linha in DIR.readlines():
            list_of_path.append(linha)
            DIR.close()
        if len(list_of_path)!=0:
            return list_of_path
    except:
        print("Error!!")

    finally:
        print("Funcao Executada!")

    
    
    

def mainVoice(Query):
    frases=extrairFrasesDB(Query)
    vetor=criarArquivosMP3(frases)
    createArqVoice(vetor)

