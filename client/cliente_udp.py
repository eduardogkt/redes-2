import socket
import time
import sys


def run_client(metrica, tam_pacote, info, host):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(3)

    server_ip = socket.gethostbyname(host)
    server_port = 8000

    requisicao = f"{metrica} {tam_pacote} {info}"
    client.sendto(requisicao.encode(), (server_ip, server_port))

    recebe_dados(client, tam_pacote, info, server_port)

    client.close()
    print("Transmissão finalizada")
    print("=============================================================================")
    
def recebe_dados(client, tam_pacote, info, server_port):
    print("Abrindo arquivo e preparando para receber os pacotes...")
    f = open(info, 'wb')
    print(f'Recebendo pacotes de tamanho... {tam_pacote}')
    pacotes_recebidos = 0
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
        except client.timeout:
            break
        #print(f'recebeu1 {data}')
    end_time = time.time()
    f.close()
    print(f"Tempo de recebimento TCP de um arquivo: {end_time - init_time}")
    print(f"Número de pacotes recebidos: {pacotes_recebidos}")

    client.sendto(str(pacotes_recebidos).encode(),(server_addr, server_port))


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