#!/usr/bin/env python

import socket
import sys
import threading
import time

BUFFER_SIZE = 1024

global number_of_servers
global port
global lider


#Array que ira conter os IDS dos Determinados IPS e suas conexoes
serverFile = []

#Classe com os objetos IP e ID
class serverFileClass (object):
    def __init__ (self, IP, ID, tcp_client):
        self.IP = IP
        self.ID = ID
        self.session = tcp_client

#Funcao que retorna o ip da maquina que o peer esta rodando
def getMyIP():
    return socket.gethostbyname(socket.gethostname())

def Urgency():
    global serverFile
    global lider
    MESSAGE = "Alguem morreu " 
    lider= serverFile[0].ID #proximo lider da lista
    for i in range(len(serverFile)):
        if(serverFile[i].IP!=getMyIP()):
            serverFile[i].session.send(MESSAGE, socket.MSG_OOB)
        elif(serverFile[i].ID == lider):
            print "Lider: ",lider
            print "Eu sou o lider"

#Funcao que fica escutando a porta 
def serverListen(conn, addr):
    global heartbeatReceive
    last_msg = time.time()
    while True:
        data = conn.recv(BUFFER_SIZE)
        if (data != ""):
            print "Recebi a mensagem:", data
            last_msg = time.time()
        if (time.time() - last_msg > 5):
            print "Parei de receber mensagens de "+ addr[0]
            for obj in serverFile:
                if(obj.IP == addr[0]):
                    print "Removi "+obj.IP+" do vetor" 
                    if (obj.ID == lider):
                        print "Lider morreu: ",lider
                        serverFile.remove(obj)
                        Urgency()
                    else:
                        serverFile.remove(obj)
                    print "Veja o vetor: ["
                    for i in range(0,len(serverFile)):
                        print "("+serverFile[i].IP+", "+ str(serverFile[i].ID)+ ", socket)"        
                    print "]"
            break;


#Inicia o servidor em determinada porta, para cada sessao tcp conectada cria
#uma thread que tem como funcao sempre ficar escutando o que a sessao tcp envia
def server():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Criei um socket TCP"
    tcp_server.bind((getMyIP(), port))
    print "Conectei a porta",port
    tcp_server.listen(1)
    print "Comecei a escutar"
    while True:
        conn, addr = tcp_server.accept()
        print addr[0]+" se conectou"
        threadServerListen = threading.Thread(target= serverListen, args=(conn, addr))
        threadServerListen.daemon = True
        threadServerListen.start()
    conn.close()

#Envia um heartbeat, consiste percorrer o array que guarda os estados da conexao e para cada sessao da um send.
def heartbeat():
    global serverFile
    while True: 
        time.sleep(5)
        for i in range (0, len(serverFile)):
            if(serverFile[i].IP != getMyIP()):
                MESSAGE = "Sou o " + getMyIP() + ' Estou Vivo' 
                serverFile[i].session.send(MESSAGE)
#        tcp_client.close()

#Gera um array de objetos que guarda o estado da sessao para cada ip
def generateSessionObject():
    global serverFile
    global lider
    time.sleep(5)
    for i in range (0, len(serverFile)):
        if (serverFile[i].IP != getMyIP()):
            tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print "Criei um socket TCP"
            tcp_client.connect((serverFile[i].IP, port))
            print "Conectei ao servidor ",serverFile[i].IP
            serverFile[i].session = tcp_client
            print "Adicionei a conexao com "+ serverFile[i].IP+ " ao vetor"
            print "Veja o vetor: ["
            for i in range(0,len(serverFile)):
                print "("+serverFile[i].IP+", "+ str(serverFile[i].ID)+ ", None)"        
            print "]"
    lider = 0
    print "Realizei conexao com todos os peers"
    print "Lider inicia igual a 0"
    for i in range (0,len(serverFile)):
        if (serverFile[i].IP == getMyIP()):
            if(serverFile[i].ID == lider):
                print "Sou o peer lider"

#Leitura do arquivo com o ip e ids dos servidores
def openFile():
    global port
    global number_of_servers
    global serverFile
    print "Abri o arquivo"
    with open('server.txt', 'r') as arq:
        print "Processei os dados do arquivo"
        print "Veja os dados: "
        first_line = arq.readline() #pega a primeira linha
        first_line = first_line.split() 
        number_of_servers = first_line[0]
        print "Numero de servidores:",number_of_servers  
        port = int(first_line[1])
        print "Numero da porta:",port
        for line in arq:
            valores = line.split()
            serverFile.append(serverFileClass(valores[0], int(valores[1]),None))
            print "Inseri IP:"+valores[0]+" e ID:"+valores[1]+" ao vetor"
        print "Veja o vetor: ["
        for i in range(0,len(serverFile)):
            print "("+serverFile[i].IP+", "+ str(serverFile[i].ID)+ ", None)"       
        print "]" 
        arq.close()


#-----------------------------MAIN-------------------------------#

print "=============================================================="
print "Trabalho Pratico REDES II 2017/1 - Prof. Elias P. Duarte Jr."
print "Aluno:Fernando Claudecir Erd - GRR20152936 - fce15"
print "Aluno:Gabriela Yukari Kimura - GRR20151446 - gyk15"
print "==============================================================\n"
print "PEER 0"
print "Iniciei o vetor"
print "O vetor estah vazio"
print "Veja o vetor: [ ]"
openFile()

for i in range(0,len(serverFile)):
    if(serverFile[i].IP == getMyIP()):
        print "Iniciei peer com o IP:"+serverFile[i].IP+ " e ID:"+ str(serverFile[i].ID)

#Inicio de Threads
threadServer = threading.Thread(target=server)
threadServer.daemon = True
threadServer.start()
generateSessionObject()
heartbeat()
