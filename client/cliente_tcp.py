import socket
import time
import sys


def run_client(metrica, tam_pacote, nome_arquivo, host, num_bytes):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname(host)
    server_port = 8000

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
    requisicao = f"{metrica} {tam_pacote} {nome_arquivo} {num_bytes}"
    client.send(requisicao.encode())

    print("Abrindo arquivo e preparando para receber os pacotes...")
    f = open(nome_arquivo, 'wb')
    print(f'Recebendo pacotes de tamanho... {tam_pacote}')

    data =  client.recv(tam_pacote)
    init_time = time.time()
    while True:
        if (data == b''):
            break
        f.write(data)
        data = client.recv(tam_pacote)
        #print(f'recebeu1 {data}')
    end_time = time.time()
    f.close()
    print('Acabou a transmissão')

    final_time = round(end_time - init_time, 3)
    print(f"Tempo de recebimento TCP de um arquivo: {final_time} segundos")
  
    


print("=============================================================================")
print("Inicio da execução: programa que calcula métricas TCP lado cliente")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print("=============================================================================")



if len(sys.argv) < 4:
    print("Número de argumentos errados")
    sys.exit(1)

metrica = sys.argv[1].lower()              # Tipo arquivo ou memória
tam_pacote = int(sys.argv[2])              # Tamanho do pacote a cada 
nome_arquivo = sys.argv[3].lower()
host = sys.argv[4]
num_bytes = int(sys.argv[5])


run_client(metrica, tam_pacote, nome_arquivo, host, num_bytes)