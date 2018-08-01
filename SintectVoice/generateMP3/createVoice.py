#!/usr/bin/env python

#IMport ggts Google

from gtts import gTTS
# execute mp3 imports
import subprocess as s
# importando classes de subdiretorios
import sys
sys.path.append("../db_")
sys.path.append("generates")
from lsblooDB import Querys
## manipular arquivos e diretorios
import os
import os.path

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
    extensoes=[]
    for i in frases_VETOR:            
        criarArquivomp3 = gTTS(i,lang="pt")
        aux += i
        aux += '.'
        aux += extensao
        verifc = os.path.isfile("/home/osvaldoairon/Área de Trabalho/SintectVoice/generateMP3/generates/%s"%(aux))
        #print(aux)
        if verifc:
            aux=''
            print("pass! arq!")
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
    a.insertD("01/08/2018","bom?")
    frases =[]
    a.resultset()
    vetor = []
    vetor = a.resultset()

    for i in vetor:
        frases.append(i[1])
        #print(i[1])
    return frases
def createArqVoice(arquivomp3Audio):

    try:
        meuPlayer='mplayer'
        #print(extensoes[6])
        for i in arquivomp3Audio:
            s.call([meuPlayer,i])
    except IndexError:
        pass
    
    



a = Querys()
frases=extrairFrasesDB(a)
vetor=criarArquivosMP3(frases)
createArqVoice(vetor)
