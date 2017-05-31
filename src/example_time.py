#!/usr/bin/python
import time

while True:
    old_time = time.time()
    print "Old", old_time
    
    current_time = time.time()
    while (current_time - old_time < 10):
            current_time = time.time()
    print "Vou Enviar Mensagem Pela Rede"
