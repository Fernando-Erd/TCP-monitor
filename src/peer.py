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

#-----------------------------SERVIDOR-------------------------------#
def server():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Iniciei o server"
    tcp_server.bind((TCP_IP, port))
    tcp_server.listen(1)
    conn, addr = tcp_server.accept()
    print "Endereco da Conexao, Processo:", addr
    while True:
        data = conn.recv(BUFFER_SIZE)
        print "Mensagem:", data
        if (data == "sair"):
            break;
        conn.send(data)  # echo
    conn.close()

#-----------------------------CLIENT--------------------- ----------#
def client():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True: 
        old_time = time.time()
        current_time = time.time()
        while (current_time - old_time < 10):
            current_time = time.time()
        for i in range (0, len(ip_id_objects)):
            MESSAGE = "Sou o " + ip_id_objects[i].IP + ' Estou Vivo' 
            tcp_client.connect((ip_id_objects[i].IP, port))
            tcp_client.send(MESSAGE)
        tcp_client.close()

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
print "Numero de Servidores:", number_of_servers
print "Porta:", port
for i in range(0, len(ip_id_objects)):
    print ip_id_objects[i].ID, ip_id_objects[i].IP

#Inicio de Threads
threadServer = threading.Thread(target=server)
threadServer.daemon = True
threadServer.start()
client()
