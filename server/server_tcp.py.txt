import socket
import time
import sys

def run_server(host, server_port):
    # Criando o socket do servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname(host)

    # Associa o socket ao endereço local e porta específicos
    server.bind((server_ip, server_port))


    # escuta, a espera de pedidos de conexão
    server.listen(0)

    print(f"Escutando em {server_ip}:{server_port}...")

    cliente, cliente_addr = server.accept() 
    print(f"Recebeu conexão em {cliente_addr}")

    while True:
        # Recebe a requisição do cliente
        data, cliente_addr = cliente.recvfrom(1024)
        data = data.decode()
        msg = data.split()
        tam_pacote = int(msg[1])
        nome_arquivo = msg[2]
        num_bytes = int(msg[3])

        if msg[0] == "arquivo":
            mandando_arquivo(cliente, tam_pacote, nome_arquivo)
        else:
            mandando_memoria_principal(cliente, tam_pacote, num_bytes)
        break

    # desaloca socket do cliente
    cliente.close()           
    # desaloca socket do servidor
    server.close()
    print("Transmissão finalizada")
    print("=============================================================================")
    print()

# Manda um arquivo solicitado pelo o cliente e calcula o tempo de envio
def mandando_arquivo(cliente, tam_pacote, nome_arquivo):
    print(f"Mandando o arquivo {nome_arquivo} para cliente TCP")
    print(f"Mandando {tam_pacote} bytes por vez... ")
    f = open(nome_arquivo,'rb')

    # Começo do envio
    init_time = time.time()
    data = f.read(tam_pacote)
    while(data != b''):
        cliente.send(data)
        data = f.read(tam_pacote)
        
    f.close()
    end_time = time.time()
    final_time = round(end_time - init_time, 5)

    print(f"Tempo de envio do arquivo do servidor TCP: {final_time} segundos")


def mandando_memoria_principal(cliente, tam_pacote, num_bytes):
    data = b'a' * num_bytes
    print(f"Mandando um dado de {num_bytes} bytes em memória principal para o cliente TCP")
    print(f"Mandando {tam_pacote} bytes por vez... ")

    init_time = time.time()
    for i in range(0, len(data), tam_pacote):
        cliente.send(data[i:i+tam_pacote])

    end_time = time.time()
    final_time = round(end_time - init_time, 5)
    print(f"Tempo de envio do servidor UDP de {num_bytes} bytes em memoria principal: {final_time} segundos")



if len(sys.argv) < 2:
    print("Número de argumentos errados")
    print(f"Uso: python3 {sys.argv[0]} <host> <server_port>")
    sys.exit(1)
host = sys.argv[1]                                # Host do servidor
server_port = int(sys.argv[2])                    # Porta do servidor             

print("=============================================================================")
print("Inicio da execução: programa que calcula métricas TCP lado servidor")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print()

run_server(host, server_port)
