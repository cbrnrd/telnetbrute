import socket
import sys
import os
import telnetlib

def generate_random_ipv4():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def default_logins():
    logins = {
    'admin' : 'admin',
    
    }

def telnetscan(host, port=23):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = s.connect_ex((host, port))
        if code == 0:
            return True
        sock.close()
    except Exception as e:
        return False


def brute(host):
    # Do bruting of host (using logins as defuned above)

def print_help():
    print """
        Usage: python telnetbrute.py [VERBOSE] [SHODAN] [-h]

        SHODAN:         Search with shodan instead of custom scanner (Shodan module required)
        VERBOSE:        Print extra information messages
        -h:             Show this help message

    """

def main():
    verbose = False
    shodan = False

    for _ in range(len(sys.argv[])):
        if sys.argv[_] == "VERBOSE":
            verbose = True
        elif sys.argv[_] == "SHODAN":
            shodan = True
        elif sys.argv[_] == "-h":
            print_help()
        else:
            print_help()

    # Try to import the shodan module        
    if shodan == True:
        try:
            import shodan
        except ImportError:
            print "Shodan required. Install it by using `pip install shodan`"

            #TODO do more stuff here

    while True:
        ip = generate_random_ipv4
        if verbose:
            print "Scanning: {}".format(ip)
        openport = telnetscan(ip)

        # If port 23 isn't open
        if not openport:
            pass
        else:
            brute(ip)
    

if __name__ == "__main__":
    main()

'''
def test_connection(server, port):
    
    
while True:
    sleep(30000) # retry connection every 20 seconds
    connstat = test_connection(server, port)
    if connstat == 0:
        connect(server, port)
    else:
        pass
        '''
