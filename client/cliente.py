import socket
import time



def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname("i24")
    server_port = 8001

    # envia pedido de conexão para o cliente
    try:
        client.connect((server_ip, server_port))
        print("Conectado com sucesso")
    except socket.error as e:
        print(f"Failed to connect: {e}")
    
    calculate_time_tcp(client)


    """
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
    
    """
    # desaloca socket, encerrando conexão com o server
    while True:
        # recebe resposta do server
        response = client.recv(1024)
        response = response.decode("utf-8")

        # se recebeu closed do server indica que server encerrou a conexão
        if response.lower() == "closed":
            break

        print(f"Received: {response}")

    client.close()
    print("Connection to server closed")


def calculate_time_tcp(client):
    print("Mandando arquivo para TCP...")
    f = open('img1.jpeg','rb')


    init_time = time.time()
    data = f.read(1024)
    while(data):
        client.send(data)
        data = f.read(1024)
        print('entrou')
    f.close()
    end_time = time.time()

    print(f"Tempo de envio TCP: {end_time - init_time}")


run_client()