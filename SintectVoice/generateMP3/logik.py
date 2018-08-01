## Create Lgic chat
# Criar parte de logica entre o MP3 salvo e as minhas frases de input
#
import sys
import os
import os.path
sys.path.append("../db_")
sys.path.append("../generateMP3")
from createVoice import mainVoice,loadPatchTXT
from lsblooDB import Querys
#Preciso dos dados do banco
# preciso dos arquivos MP3
# preciso da entrada do usuario
import subprocess as s
import time

meuPlayer='mplayer'



def executeMainC():
    """
    Envia um objeto do tipo Querys pra executar o Gerador
    """
    a = Querys()
    mainVoice(a)

def say(say1):
    helpi=[]
    """
    Carrega os paths do TXT
    e utiliza o modulo os para carregar o sist de arqs
    """
    eqo=''
    vetor_paths = loadPatchTXT()
    eqo += say1
    eqo += ".mp3"
    #print(vetor_paths)
    print(eqo)
    x=0
    cont = 0
    for k in vetor_paths:
        helpi.append(os.path.basename(k))
    
    for x in range(len(helpi)):
        print(helpi[x].strip())
        if helpi[x].strip() == eqo.strip():
            print("XD!")
            cont = x
            break
    if cont!=0:
        print("oks!")
        saida=str(vetor_paths[cont])
        
        print(saida)
        #DEU DOIDERA AQUI 
        s.call([meuPlayer,'/home/osvaldoairon/Área de Trabalho/SintectVoice/generateMP3/generates/bom?.mp3'])
        
        
            
    
       

def logik(vetor,inpt):
    #Ideia inicial pegar a entrada do usuario, criar um algoritmo que entenda
    #algumas strings e com base nisso faça a katia executar o mp3
    
    #print(vetor_paths)
    helpi=[]
    helpi.append(inpt)
    for k in vetor:
        if k == helpi[0]:
            return k
            break
    
            
    
def testInputText():
    inpt=str(input("Digite o texto: "))
    return inpt
def xnFF():
    my_result=[]
    says=[]
    a = Querys()
    my_result = a.resultset()
    for x in my_result:
        says.append(x[1])
    return says
executeMainC()

say(logik(xnFF(),testInputText()))
