from socket import *
import threading
class UdpClient:
    def __init__(self,ip='127.0.0.1',port=9998):
        self.ip = ip
        self.port = port
        self.sock = socket(type=SOCK_DGRAM)
    def start(self):
        self.send('reg')
        threading.Thread(target=self.recv).start()
    def stop(self):
        self.sock.close()
    def recv(self):
        while True:
            data = self.sock.recv(1024)
            print(data)
    def send(self,mes):
        data = mes.encode()
        self.sock.sendto(data,(self.ip,self.port))

if __name__ == '__main__':
    client = UdpClient()
    client.start()

    while True:
        cmd = input('>>>')
        if cmd == 'stop':
            client.stop()
            break
        client.send(cmd)