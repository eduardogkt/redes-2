import socket
import time
import sys


def run_client(metrica, tam_pacote, nome_arquivo, num_bytes,host, server_port):
    # Criando o socket do cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)

    server_ip = socket.gethostbyname(host)

    # Mandando requisição dos dados para o servidor
    requisicao = f"{metrica} {tam_pacote} {nome_arquivo} {num_bytes}"
    client.sendto(requisicao.encode(), (server_ip, server_port))

    recebe_dados(client, tam_pacote, nome_arquivo, server_ip ,server_port)

    client.close()
    print("Transmissão finalizada")
    print("=============================================================================")
    
def recebe_dados(client, tam_pacote, info, server_ip, server_port):
    print("Abrindo arquivo e preparando para receber os pacotes...")
    f = open(info, 'wb')
    print(f'Recebendo pacotes de tamanho {tam_pacote}...')
    pacotes_recebidos = 0

    # Calculando o tempo e recebendo pacotes
    data, server_addr =  client.recvfrom(tam_pacote)
    pacotes_recebidos += 1
    init_time = time.time()
    while True:
        if (data == b'EOF'):
            break
        f.write(data)
        try:    
            data, server_addr = client.recvfrom(tam_pacote)
            pacotes_recebidos += 1
        except socket.timeout:
            print("Ocorreu Timeout")
            break
        
    end_time = time.time()
    f.close()
    final_time = round(end_time - init_time, 5)
    print("Acabou a transmissão")
    print(f"Tempo de recebimento UDP de um arquivo: {final_time} segundos")
    print(f"Número de pacotes recebidos: {pacotes_recebidos}")

    pacotes = str(pacotes_recebidos)
    client.sendto(pacotes.encode(), (server_ip, server_port))


print("=============================================================================")
print("Inicio da execução: programa que calcula métricas TCP lado cliente")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print("=============================================================================")



if len(sys.argv) < 4:
    print("Número de argumentos errados")
    sys.exit(1)

metrica = sys.argv[1].lower()              # Tipo arquivo ou memória
tam_pacote = int(sys.argv[2])              # Tamanho do pacote a cada 
nome_arquivo = sys.argv[3].lower()         # Arquivo onde será escrito os dados
num_bytes = int(sys.argv[4])               # Número de bytes que será transferido em memória
host = sys.argv[5]                         # Nome do host do servidor
server_port = sys.argv[6]                  # Porta do servidor


run_client(metrica, tam_pacote, nome_arquivo, num_bytes,host, server_port)