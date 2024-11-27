import socket
import time



def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname("h44")
    server_port = 8001

    # envia pedido de conexão para o cliente
    try:
        client.connect((server_ip, server_port))
        print("Conectado com sucesso")
    except socket.error as e:
        print(f"Failed to connect: {e}")
    
    #calculate_time_tcp(client)
    #time_tcp_ram(client)
    #client.close()

    while True:
        # manda mensagem para o cliente
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024])

        # recebe resposta do server
        response = client.recv(1024)
        response = response.decode("utf-8")

        # se recebeu closed do server indica que server encerrou a conexão
        if response.lower() == "closed":
            break

        print(f"Received: {response}")
    
    # desaloca socket, encerrando conexão com o server
   

def calculate_time_tcp(client):
    print("Mandando arquivo para TCP...")
    f = open('19mb.txt','rb')


    init_time = time.time()
    data = f.read(1024)
    while(data):
        client.send(data)
        data = f.read(60000)
        
    f.close()
    message = b'finished'
    client.send(message)
    end_time = time.time()

    print(f"Tempo de envio TCP: {end_time - init_time}")


def time_tcp_ram(client):
    data= b'a' * 1000000000
    print("Mandando  para TCP em memoria principal...")
    init_time = time.time()
    chunk_size = 1024
    for i in range(0, len(data), chunk_size):
        client.send(data[i:i+chunk_size])
    message = b'finished'
    client.send(message)
    end_time = time.time()  
    print(f"Tempo de envio TCP: {end_time - init_time}")

run_client()