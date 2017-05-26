#!/usr/bin/env python

import socket
import sys
import threading

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
TCP_PORT = 8123
#-----------------------------SERVIDOR-------------------------------#
def server():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((TCP_IP, TCP_PORT))
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

#-----------------------------CLIENT-------------------------------#
def client():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((TCP_IP, TCP_PORT))
    while True:
        MESSAGE = raw_input()
        tcp_client.send(MESSAGE)
        data = tcp_client.recv(BUFFER_SIZE)
        #Encerrando o Loop
        if (MESSAGE == "sair"):
            break
    tcp_client.close()
    print 'received data:', data

#-----------------------------MAIN-------------------------------#

threadServer = threading.Thread(target=server)
#threadServer.daemon = True
threadServer.start()
client()
