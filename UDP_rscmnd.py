import sys
import socket
from subprocess import Popen, PIPE
import time
from datetime import datetime

port = 0

def parse_arguments():
    if len(sys.argv) != 3:
        print "Usage :- ~$ <rscmnd> -p <port-number> -h <help>"
    else:
        for i in range(1, len(sys.argv), 2):
            if sys.argv[i] == '-p':
                global port
                port = int(sys.argv[i + 1])
            else:
                print "Usage :- ~$ <rscmnd> -p <port-number> -h <help>"

if __name__ == "__main__":
    parse_arguments()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    while True:
        input_message, address = sock.recvfrom(1024)
        if input_message:
            print input_message
            split_message = input_message.split('-')
            command = split_message[0]
            execution_count = int(split_message[1])
            timeDelay = int(split_message[2])
            for j in range(0, execution_count):
                out = Popen(command, shell=True, stdout=PIPE).stdout.read()
                sock.sendto(out, address)
                print datetime.now()
                time.sleep(timeDelay)
