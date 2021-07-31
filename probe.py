import socket
from sys import argv

ADDR='localhost'
PORT=80
PORTB=PORT

SCAN=False
GETBANNER=False
VERBOSE=False

USEAGE="""\n\tUSEAGE:
\n\t -a TARGET_ADDRESS -p TARGET_PORT [-s N] [-b] [-h] [-v]
\n\t -b = Get Banner from service if available
\n\t -h = Show this help message
\n\t -s = Scan ports from -p TARGET_PORT to -s N inclusively
\n\t -v = Be verbose about information
"""

def getBanner(port):
    socket.setdefaulttimeout(1)
    try:
        s=socket.socket()
        if VERBOSE: print(f'Get banner from {ADDR} on {port}')
        s.connect((ADDR, PORT))
        banner=s.recv(1024)
        s.close()
        print(f'Banner: {banner}')
    except Exception as e:
        pass

def poke(addr='127.0.0.1', port=80):
    if VERBOSE: print(f'Poke: {addr}:{port}')
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((addr, port))==0:
            print(f'Port {port} is OPEN')
            if GETBANNER: getBanner(port)
        else:
            if VERBOSE: print(f'Port {port} is CLOSED')
        s.close()
    except Exception as e:
        pass

if __name__ == '__main__':
    if len(argv) <= 3:
        print(USEAGE)
    else:
        if '-a' in argv:
            ADDR=argv[argv.index('-a')+1]
        if '-b' in argv:
            GETBANNER=True
        if '-h' in argv:
            print(USEAGE)
        if '-p' in argv:
            PORT=int(argv[argv.index('-p')+1])
        if '-s' in argv:
            SCAN=True
            PORTB=int(argv[argv.index('-s')+1])
        if '-s' not in argv:
            PORTB=PORT
        if '-v' in argv:
            VERBOSE=True
    
    for p in range(PORT, PORTB+1):
        if VERBOSE: print()
        poke(addr=ADDR, port=p)
