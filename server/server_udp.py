import socket
from packet import packet

def run_server():
    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname("j8")
    port = 8000

    # associal o socket ao endereço local e porta específicos
    sock.bind((server_ip, port))

    while True:
        data, addr = sock.recv(1024)
        request = request.decode("utf-8") # converte para string
        
        # termina a conexão caso receba close
        if request.lower() == "close":
            # envia mensagem confirmando encerramento para cliente e sai do loop
            sock.send("closed".encode("utf-8"))
            break

        print(f"Received: {request}")

        response = "accepted".encode("utf-8")

    # desaloca socket do cliente
    sock.close()


run_server()
