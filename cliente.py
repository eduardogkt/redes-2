import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname("j8")
    server_port = 8000

    # envia pedido de conexão para o cliente
    client.connect((server_ip, server_port))

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
    client.close()
    print("Connection to server closed")

run_client()
