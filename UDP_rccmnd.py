import sys
import socket
from datetime import datetime
import time
server_name=""
port=0
command=""
execution_count=0
delay=0


def parse_arguments():
    global server_name, port, command, execution_count, delay
    for i in range(1,len(sys.argv),2):
        if sys.argv[i] == '-s':
            server_name = str(sys.argv[i+1])
            i = i+1
        elif sys.argv[i] == '-p':
            port = int(sys.argv[i+1])
            i = i+1
        elif sys.argv[i] == '-c':
            command = str(sys.argv[i+1])
            i = i+1
        elif sys.argv[i] == '-n':
            execution_count = int(sys.argv[i+1])
            i = i+1
        elif sys.argv[i] == '-d':
            delay = int(sys.argv[i+1])
            i = i+1
        else:
            print "~$ <rccmnd> -s <server-name> -p <server-port> -c <command> -n <num_exec> -d <delay>"




if __name__ == "__main__":
    parse_arguments()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_name, port)
    print server_name, port, command, execution_count, delay
    start = time.time()
    try:
        print "send data..."
	message = command + '-' + str(execution_count) + '-' + str(delay)
        sock.sendto(message, server_address)
        for j in range(0, execution_count):
            print "receive data..."
            reply, server = sock.recvfrom(1024)
            print datetime.now()
            print reply
    	end = time.time()
        RTT = end - start
    	print "Round trip time: ",RTT
    finally:
        sock.close()
