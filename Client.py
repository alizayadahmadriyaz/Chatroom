import socket
import threading

aliases=input('enter the name :')
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',59000))

def client_reciev():
    while True:
        try:
            data=client.recv(16384).decode('utf-8')
            if data=='Enter your name: ':
                client.send(aliases.encode('utf-8'))
            else:
                print(data)
        except:
            print('error')

            client.close()
            break   

def client_send() :
    while True:
        message=f'{aliases}:{input(" ")}'
        client.send(message.encode('utf-8'))

rec_thr=threading.Thread(target=client_reciev)  
snd_thr=threading.Thread(target=client_send) 
rec_thr.start()
snd_thr.start()