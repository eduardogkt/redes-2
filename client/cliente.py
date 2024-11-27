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
    
    recebe_arquivo(client, 'ex1.txt', 1024)
    recebe_arquivo(client, 'ex2.txt', 60000)

    client.close()
    
    # desaloca socket, encerrando conexão com o server

def recebe_arquivo(client, arquivo, tam_pacote):
    f = open(arquivo, 'wb')
    print(f'Recebendo pacotes de tamanho {tam_pacote}')
    data =  client.recv(tam_pacote)
    print('recebeu')
    init_time = time.time()
    while True:
        if (data < tam_pacote):
            print('recebeu finished')
            break
        f.write(data)
        print('parado')
        data = client.recv(tam_pacote)
        print(f'recebeu1 {data}')

    end_time = time.time()
    f.close()
    print('Acabou a transmissão')
    print(f"Tempo de recebimento TCP de um arquivo: {end_time - init_time}")
    
run_client()