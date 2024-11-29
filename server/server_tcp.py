import socket
import time
import sys

def run_server(host):
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname(host)
    port = 8000

    # associal o socket ao endereço local e porta específicos
    server.bind((server_ip, port))


    # escuta, a espera de pedidos de conexão
    server.listen(0)

    print(f"Escutando em {server_ip}:{port}...")

    cliente, cliente_addr = server.accept() 
    print(f"Recebeu conexão em {cliente_addr}")

    while True:
        data, cliente_addr = cliente.recvfrom(1024)
        data = data.decode()
        msg = data.split()
        tam_pacote = int(msg[1])
        info = msg[2]

        if msg[0] == "arquivo":
            mandando_arquivo(cliente, tam_pacote, info)
        else:
            mandando_memoria_principal(cliente, tam_pacote, int(info))
        break

    # desaloca socket do cliente
    cliente.close()           
    # desaloca socket do servidor
    server.close()
    print("Transmissão finalizada")

def mandando_arquivo(cliente, tam_pacote, info):
    print(f"Mandando o arquivo {info} para cliente TCP")
    print(f"Mandando {tam_pacote} bytes por vez... ")
    f = open(info,'rb')

    init_time = time.time()
    data = f.read(tam_pacote)
    while(data != b''):
        cliente.send(data)
        data = f.read(tam_pacote)
        
    f.close()
    end_time = time.time()

    print(f"Tempo de envio do arquivo do servior TCP: {end_time - init_time}")


def mandando_memoria_principal(cliente, tam_pacote, num_bytes):
    data = b'a' * num_bytes
    print(f"Mandando um dado de {num_bytes} bytes em memória principal para o cliente TCP")
    print(f"Mandando {tam_pacote} bytes por vez... ")

    init_time = time.time()
    for i in range(0, len(data), tam_pacote):
        cliente.send(data[i:i+tam_pacote])

    end_time = time.time()  
    print(f"Tempo de envio TCP de {num_bytes} bytes em memoria principal: {end_time - init_time}")


print("=============================================================================")
print("Inicio da execução: programa que calcula métricas TCP lado servidor")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print("=============================================================================")

if len(sys.argv) < 2:
    print("Número de argumentos errados")
    sys.exit(1)
host = sys.argv[1]

run_server(host)
