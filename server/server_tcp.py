import socket
import time

def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname("i24")
    port = 8001

    # associal o socket ao endereço local e porta específicos
    server.bind((server_ip, port))
    f = open('img1.jpeg', 'wb')


    # escuta, a espera de pedidos de conexão
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    while True:
        c, addr = server.accept()     # Establish connection with client.
        print ('Got connection from'), addr
        print ("Receiving...")
        l = c.recv(1024)
        while (l):
            print ("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print ("Done Receiving")
        message = "closed"
        c.send(message.encode())
        c.close()           

        # desaloca socket do cliente
        server.close()
        break


run_server()
