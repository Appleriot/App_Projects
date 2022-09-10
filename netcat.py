import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def excute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return 
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)

    return output.decode()

if name == '__main__':
    paser = argparse.ArgumentParser(description="BHP Net Tool")
    formatter_class = argparse.RawTextHelpFormatter, epilog=textwrap.dedent('''Example:
    netcat.py -t 192.168.1.108 -p 5555 -l -c #command shell
    netcat.py 192.168.1.108 -p 555 -l -u=mytest.txt #upload to file
    netcat.py 192.168.1.108 -p 5555 -l -e\"cat / etc/password" #excute command
    echo 'ABC' ./netcat.py -t 192.168.1.108 -p 135 #echo text to sever port 35
     netcat.py -t 192.168.1.108 -p 5555 #connect to server''')

paser.add_argument('-c', '--command', action='store_true', help='command shell')
paser.add_argument('-e', '--excute', help='excute specifted command')
paser.add_argument('-l', '--listen', action='store_true', help='listen')
paser.add_argument('-p', '--port', type=int, default=5555, help='specifed port')
paser.add_argument('-t', '--target', default='192.168.1.203', help='specifed IP')
paser.add_argument('-u', '--upload', help='upload file')

args = paser.parse_args()
if args.listen:
    buffer = ''
else:
    buffer = sys.stdin.read()

nc = NetCat(args, buffer.encode())
nc.run()

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                respone = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    respone += data.decode()
                    if recv_len < 4096:
                        break
                if respone:
                    print(respone)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()
    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.decode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saveed file {self.args.upload}'
            client_socket.send(message.encode())
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    respone = excute(cmd_buffer.decode())
                    if respone:
                        client_socket.send(respone.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server failed {e}')
                    self.socket.close()
                    sys.exit()
    def run(self):
        if self.args.listen():
            self.listen()
        else:
            self.send()