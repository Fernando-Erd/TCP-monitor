#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Array que ira conter os IDS dos Determinados IPS
ip_id_objects = []

#Classe com os objetos IP e ID
class IP_ID_Class (object):
    def __init__ (self, IP, ID):
        self.IP = IP
        self.ID = ID

#Leitura do arquivo com o ip e ids dos servidores
with open('server.txt', 'r') as arq:
    first_line = arq.readline()
    first_line = first_line.split()
    number_of_servers = first_line[0] 
    port = first_line[1]
    for line in arq:
        valores = line.split()
        ip_id_objects.append(IP_ID_Class(valores[0], valores[1]))
    arq.close()

print "Numero de Servidores:", number_of_servers
print "Porta:", port
for i in range(0, len(ip_id_objects)):
    print ip_id_objects[i].ID, ip_id_objects[i].IP
