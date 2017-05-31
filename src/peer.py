#!/usr/bin/env python

import socket
import sys
import threading
import time

#####################################################################
######################Variaveis Importantes##########################
# port = porta                                                      #
# ip_id_objects = array de objetos que contem IP e ID               #
# number_of_server = Numero de servidores                           #
#####################################################################

TCP_IP = '200.17.202.6'
BUFFER_SIZE = 1024

#Classe com os objetos IP e ID
class IP_ID_Class (object):
    def __init__ (self, IP, ID):
        self.IP = IP
        self.ID = ID

#Funcao que retorna o ip da maquina que o peer esta rodando
def getMyIP():
    return socket.gethostbyname(socket.gethostname())

#Funcao que fica escutando a porta 
def serverListen(conn, addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        print "Mensagem:", data


#Inicia o servidor em determinada porta, para cada sessao tcp conectada cria
#uma thread que tem como funcao sempre ficar escutando o que a sessao tcp envia
def server():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Iniciei o server"
    tcp_server.bind((getMyIP(), port))
    tcp_server.listen(1)
    while True:
        conn, addr = tcp_server.accept()
        print conn, addr
        threadServerListen = threading.Thread(target= serverListen, args=(conn, addr))
        threadServerListen.daemon = True
        threadServerListen.start()
    conn.close()


#Funcao que envia a mensagem para os outros peers
#Existe um array chamado tcps que guarda o estado da sessao para cada ip, e ao 
#percorrer esse array envia uma msg para cada peer conectado, essa msg e
#enviada a cada 5 segundos.
def client():
    tcps = []
    time.sleep(5)
    for i in range (0, len(ip_id_objects)):
        if (ip_id_objects[i].IP != getMyIP()):
            tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_client.connect((ip_id_objects[i].IP, port))
            tcps.append(tcp_client)
    while True: 
        time.sleep(5)
        for i in range (0, len(ip_id_objects)-1):
            print 'Sou o Cliente, estou me preparando para enviar uma msg'
            MESSAGE = "Sou o " + getMyIP() + ' Estou Vivo' 
            tcps[i].send(MESSAGE)
            print "Sou o Cliente, consegui enviar a mensagem"
#        tcp_client.close()

#-----------------------------MAIN-------------------------------#

#Array que ira conter os IDS dos Determinados IPS
ip_id_objects = []

#Leitura do arquivo com o ip e ids dos servidores
with open('server.txt', 'r') as arq:
    first_line = arq.readline() #pega a primeira linha
    first_line = first_line.split() 
    number_of_servers = first_line[0]  
    port = int(first_line[1])
    #pega todos os ips e ids do arquivo e guarda em um array de objetos
    for line in arq:
        valores = line.split()
        ip_id_objects.append(IP_ID_Class(valores[0], int(valores[1])))
    arq.close()

#Printa Porta, Ip e Ids
print "Iniciando peer com o ip: ", getMyIP()
print "Numero de Servidores: ", number_of_servers
print "Porta:", port
for i in range(0, len(ip_id_objects)):
    print ip_id_objects[i].ID, ip_id_objects[i].IP

#Inicio de Threads
threadServer = threading.Thread(target=server)
threadServer.daemon = True
threadServer.start()
client()
