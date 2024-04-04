#chat Room Connection-Client to clien
import threading
import socket
host='127.0.0.1'
port=59000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients=[]
aliases=[]

def broad_cast(message):
    for client in clients:
        client.send(message)
def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            broad_cast(message)
        except:
            index=clients.index(client)
            clients.remove()
            alias=aliases[index]
            broad_cast(f'{alias}  left the chat room')
            aliases.remove(alias)
            break
def recieve():
    while True:
        print('server is running  ')
        client,address=server.accept()
        print("new connection from",address)
        client.send("Enter your name: ".encode( "utf-8"))
        name=client.recv(1024).decode()
        aliases.append(name)
        clients.append(client)
        broad_cast(f"{name} has joined the chat room".encode( "utf-8") )
        # print(f"There are {len(clients)} people in this chat room now.")
        client.send('you are now connected '.encode())
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()

if  __name__=="__main__":
    recieve()

        
