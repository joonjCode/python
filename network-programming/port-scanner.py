import socket
import threading
from queue import Queue

TARGET = '127.0.0.1'

que = Queue()
open_ports = []

def portscanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((TARGET, port))
        return True
    except :
        return False

def fill_queue(port_list):
    for port in port_list:
        que.put(port)

def worker():
    while not que.empty():
        port = que.get()
        if portscanner(port):
            print(f'Port {port} is open')
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

# Need for the last part of the script
thread_list = []

# Multithreading
for t in range(100):
    thread = threading.Thread(target = worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f'Open ports are : {open_ports}')


# Brute
'''
for port in range(1, 124):
    result = portscanner(port)
    if result:
        print(f'Port {port} is open')
    else:
        print(f'Port {port} is closed')
'''