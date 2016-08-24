import socket
import sys
import datetime
import time

server_name = ""
port = 0
command = ""
execution_count = 0
delay = 0
RTT = 0

t1 = time.time()
def parse_arguments():
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '-s':
            global server_name
            server_name = sys.argv[i + 1]
        elif sys.argv[i] == '-p':
            global port
            port = int(sys.argv[i + 1])
        elif sys.argv[i] == '-c':
            global command
            command = str(sys.argv[i + 1])
        elif sys.argv[i] == '-n':
            global execution_count
            execution_count = int(sys.argv[i + 1])
        elif sys.argv[i] == '-d':
            global delay
            delay = int(sys.argv[i + 1])
        else:
            print "Usage: ~$ <rccmnd> -s <server-name> -p <server-port> -c <command> -n <num_exec> -d <delay>"


if __name__ == "__main__":
    parse_arguments()
    message = command + " " + str(delay) + " " + str(execution_count)
    IP = socket.gethostbyname(server_name)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Connected to server: ",server_name
    print "Port: ",port
    #print type(server_name), type(port)
    client_socket.connect((server_name, port))
    print "Message: ",message
    


    #client_socket.send(message)
    start = time.time()
    for j in range(0, execution_count):

        client_socket.send(message)
        received_data = client_socket.recv(1024)
	
    print "Data received is: ",received_data
    len_message = received_data[:10]
    print "First 10 bytes of the message: ",len_message[::-1]  
    print "Message length: ",int(len_message[::-1])
    
    end = time.time()
    RTT = end - start
    print "Round trip time: ",RTT
     
     	
    client_socket.close()
    print "Connection closed "
