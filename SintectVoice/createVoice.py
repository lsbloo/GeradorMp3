#
#IMport ggts Google
from gtts import gTTS
# execute mp3 imports
import subprocess as s
# importando classes de subdiretorios
import sys
sys.path.append("db_")
from lsblooDB import Querys
## manipular arquivos e diretorios
import os


frases =[]
extensoes=[]
def criarArquivosMP3(frases_VETOR):
    #print(frases)
    extensao='mp3'
    aux=''
    
    for i in frases_VETOR:
        criarArquivomp3 = gTTS(i)
        aux += i
        aux += '.'
        aux += extensao
        criarArquivomp3.save(aux)
        extensoes.append(aux)
        aux=''

    return extensoes
    

def extrairFrasesDB():
    
    a = Querys()
    #a.insertD('28/04/2017','oi tudo bem?')
    
    a.resultset()
    vetor = []
    vetor = a.resultset()

    for i in vetor:
        frases.append(i[1])
        #print(i[1])
    
def createArqVoice(arquivomp3Audio):
    meuPlayer='mplayer'
    print(extensoes[6])
    for i in extensoes:
        s.call([meuPlayer,i])




extrairFrasesDB()
criarArquivosMP3(frases)
createArqVoice(extensoes)
