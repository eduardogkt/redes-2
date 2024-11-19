import socket

def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname("j8")
    port = 8000

    # associal o socket ao endereço local e porta específicos
    server.bind((server_ip, port))

    # escuta, a espera de pedidos de conexão
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # aceita a conexão
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # converte para string
        
        # termina a conexão caso receba close
        if request.lower() == "close":
            # envia mensagem confirmando encerramento para cliente e sai do loop
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"Received: {request}")

        response = "accepted".encode("utf-8")

        # envia mensagem de aceitação para cliente
        client_socket.send(response)

    # encerra socket do cliente
    client_socket.close()
    print("Connection to client closed")

    # desaloca socket do cliente
    server.close()


run_server()
