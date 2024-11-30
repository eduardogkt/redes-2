import socket
import time
import sys


def run_client(metrica, tam_pacote, nome_arquivo, num_bytes,host, server_port):
    # Criando o socket do cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname(host)

    print("Cliente conectando com o servidor...")
    # envia pedido de conexão para o cliente
    try:
        client.connect((server_ip, server_port))
        print("Conectado com sucesso!")
    except socket.error as e:
        print(f"Falha na conexão com o servidor: {e}")
        sys.exit()
    
    recebe_dados(metrica, client, tam_pacote, nome_arquivo, num_bytes)

    client.close()
    print("Transmissão finalizada")
    print("=============================================================================")

def recebe_dados(metrica, client, tam_pacote, nome_arquivo, num_bytes):

    # Mandando requisição dos dados para o servidor
    requisicao = f"{metrica} {tam_pacote} {nome_arquivo} {num_bytes}"
    client.send(requisicao.encode())

    print("Abrindo arquivo e preparando para receber os pacotes...")
    f = open(nome_arquivo, 'wb')
    print(f'Recebendo pacotes de tamanho {tam_pacote}...')

    # Calculando o tempo e recebendo pacotes
    data =  client.recv(tam_pacote)
    init_time = time.time()
    while True:
        if (data == b''):
            break
        f.write(data)
        data = client.recv(tam_pacote)
    end_time = time.time()
    f.close()
    print('Acabou a transmissão')

    final_time = round(end_time - init_time, 5)
    print(f"Tempo de recebimento TCP de dados: {final_time} segundos")



if len(sys.argv) < 4:
    print("Número de argumentos errados")
    print(f"Uso: python3 {sys.argv[0]} <metrica> <tam_pacote> <nome_arquivo> <num_bytes> <host> <port>")
    sys.exit(1)

metrica = sys.argv[1].lower()              # Tipo arquivo ou memória
tam_pacote = int(sys.argv[2])              # Tamanho do pacote a cada 
nome_arquivo = sys.argv[3].lower()         # Arquivo onde será escrito os dados
num_bytes = int(sys.argv[4])               # Número de bytes que será transferido em memória
host = sys.argv[5]                         # Nome do host do servidor
server_port = int(sys.argv[6])             # Porta do servidor

print("=============================================================================")
print("Inicio da execução: programa que calcula métricas TCP lado cliente")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print("=============================================================================")

run_client(metrica, tam_pacote, nome_arquivo, num_bytes,host, server_port)