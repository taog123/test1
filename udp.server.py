from socket import *
import threading
class UdpServer:
    def __init__(self,ip='127.0.0.1',port=9998):
        self.ip = ip
        self.port = port
        self.sock = socket(type=SOCK_DGRAM)
        self.sock.bind((self.ip,self.port))
        self.event = threading.Event()
        self.clients = set()
    def start(self):
        threading.Thread(target=self.recv).start()

    def recv(self):
        while not self.event.is_set():
            data,client = self.sock.recvfrom(1024)
            mes = data.decode()
            if mes == 'reg':
                self.clients.add(client)
                print('++{}'.format(self.clients))
                continue
            print(mes)
            data = 'from{}:{}'.format(client,mes).encode()
            self.send(data)

    def stop(self):
        self.event.set()
        self.sock.close()

    def send(self,data):
        for client in self.clients:
            print(client)
            self.sock.sendto(data,client)

if __name__ == '__main__':
    client = UdpServer()
    client.start()
    while True:
        cmd = input('>>>')
        if cmd == 'stop':
            client.stop()
            break