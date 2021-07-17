from socket import *

def poke(addr='localhost', port=8890):
    conn=None
    buff=''
    
    try:
        print('attempting connection')
        conn = socket(AF_INET, SOCK_STREAM)
    except Exception as e:
        print(e)
        return(-1)
    finally:
        if conn != None:
            try:
                print(f'Connecting to {addr}:{port}')
                conn.connect((addr, port))
            except Exception as e:
                print(e)
                return(-1)
            finally:
                print('sending newline')
                conn.send(b'\r\n')
                print('attempting receive')
                buff=conn.recv(1024)
                print(f'received: {buff}')
                print('closing connection')
                conn.close()
            return(0)
        else:
            print('Failed to create connection')
            return(1)
    return(-2)

print(f'Return Code: {poke(addr="www.google.com", port=443)}')
