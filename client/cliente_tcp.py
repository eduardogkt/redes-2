import socket
import time
import sys


def run_client(metrica, tam_pacote, info, host):
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
    
    recebe_dados(metrica, client, tam_pacote, info)

    client.close()
    print("Transmissão finalizada")
    print("=============================================================================")

def recebe_dados(metrica, client, tam_pacote, info):
    requisicao = f"{metrica} {tam_pacote} {info}"
    client.send(requisicao.encode())

    print("Abrindo arquivo e preparando para receber os pacotes...")
    f = open(info, 'wb')
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
    print(f"Tempo de recebimento TCP de um arquivo: {end_time - init_time}")
    


print("=============================================================================")
print("Inicio da execução: programa que calcula métricas TCP lado cliente")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print("=============================================================================")



if len(sys.argv) < 4:
    print("Número de argumentos errados")
    sys.exit(1)

metrica = sys.argv[1].lower()
tam_pacote = int(sys.argv[2])
info = sys.argv[3].lower()
host = sys.argv[4]

run_client(metrica, tam_pacote, info, host)