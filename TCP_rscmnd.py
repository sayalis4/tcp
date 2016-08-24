# TCP Server
import SocketServer
import os
import socket
import sys
from subprocess import Popen, PIPE
import datetime
import time

port = 0


def parse_arguments():
    if len(sys.argv) != 3:
        print "Usage :- ~$ <rscmnd> -p <port-number> -h <help>"
    else:
        for i in range(1, len(sys.argv), 2):
            if sys.argv[i] == '-p':
                global port
                port = sys.argv[i + 1]
            else:
                print "Usage :- ~$ <rscmnd> -p <port-number> -h <help>"



if __name__ == "__main__":
    parse_arguments()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    while 1:
        clientSocket, clientAddress = s.accept()
        data = clientSocket.recv(1024)
        print "Data: ",data
        IP = socket.gethostbyname('localhost')
        print "Connected to IP:   ",IP
        message = data.split(" ")
        
        command = message[0]
        print "Executing command:   ",command
        delay = int(message[1])
        execution_count = int(message[2])
        for j in range(0, execution_count):
            #p = Popen(message[0], shell=True, stdout=PIPE, stderr=PIPE)
            #out, err = p.communicate()
            out = Popen(message[0], shell=True, stdout=PIPE).stdout.read()
            t = datetime.datetime.now()
            print out,'\t', t
            
	    number =  len(out) + len(str(t))
              
    	    print "Length of the message is: ",number
            length =""
            while number:
	   	digit = number % 10
	   	number //= 10
	   	#print digit
    		length+=str(digit) 
		m = len(length)
	    string =  length[::-1].zfill(10) 
	    print "Message length with fixed size of 10 bytes: ",string[::-1]
				
            clientSocket.send(str(string[::-1]) + "\n" + out.rstrip() + "\n" + str(t))
            time.sleep(delay)
        t2 = time.time()
	
	
    clientSocket.close()
