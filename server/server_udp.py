import socket
import time
import sys

def run_server(host, server_port):
    # Criando o socket do servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_ip = socket.gethostbyname(host)

    # associal o socket ao endereço local e porta específicos
    server.bind((server_ip, server_port))

    print(f"Socket associado em {server_ip}:{server_port}...")

    while True:
        data, cliente_addr = server.recvfrom(1024)
        data = data.decode()
        msg = data.split()
        tam_pacote = int(msg[1])
        nome_arquivo = msg[2]
        num_bytes = int(msg[3])
        
        if msg[0] == "arquivo":
            pacotes_enviados = mandando_arquivo(server, cliente_addr, tam_pacote, nome_arquivo)
        else:
            pacotes_enviados = mandando_memoria_principal(server, cliente_addr, tam_pacote, int(num_bytes))
        print(pacotes_enviados)
        # Recebe resposta do cliente quantos pacotes ele recebeu
        data, cliente_addr = server.recvfrom(1024)
        pacotes_recebidos = int(data.decode())
        break

    # Calcula as métricas
    porcentagem = (pacotes_recebidos / pacotes_enviados) * 100
    porcentagem_arrendondada = round(porcentagem, 2)
    print(f"O servidor UDP enviou {pacotes_enviados} e o cliente UDP recebeu {pacotes_recebidos}")
    print(f"O cliente UDP recebeu {porcentagem_arrendondada}% dos pacotes enviados ")
    
    # desaloca socket do servidor
    server.close()
    print("Transmissão finalizada")
    print("=============================================================================")

# Manda um arquivo solicitado pelo o cliente e calcula o tempo de envio
def mandando_arquivo(server, cliente_addr, tam_pacote, nome_arquivo):
    print(f"Mandando o arquivo {nome_arquivo} para cliente UDP")
    print(f"Mandando {tam_pacote} bytes por vez... ")
    f = open(nome_arquivo,'rb')
    pacotes_enviados = 0

    # Começo do envio
    init_time = time.time()
    data = f.read(tam_pacote)
    while(data != b''):
        server.sendto(data, cliente_addr)
        pacotes_enviados  += 1
        data = f.read(tam_pacote)
    f.close()
    # Manda fim de arquivo
    server.sendto(b'EOF', cliente_addr)
    pacotes_enviados += 1
    end_time = time.time()

    final_time = round(end_time - init_time, 5)
    print(f"Tempo de envio do arquivo do servidor UDP: {final_time} segundos")

    return pacotes_enviados

def mandando_memoria_principal(server, cliente_addr, tam_pacote, num_bytes):
    data = b'a' * num_bytes
    print(f"Mandando um dado de {num_bytes} bytes em memória principal para o cliente UDP")
    print(f"Mandando {tam_pacote} bytes por vez... ")
    pacotes_enviados = 0

    init_time = time.time()
    for i in range(0, len(data), tam_pacote):
        server.sendto(data[i:i+tam_pacote], cliente_addr)
        pacotes_enviados += 1

    print("mandando EOF")
    server.sendto(b'EOF', cliente_addr)
    pacotes_enviados += 1
    end_time = time.time()
    final_time = round(end_time - init_time, 5)
    print(f"Tempo de envio do servidor UDP de {num_bytes} bytes em memoria principal: {final_time}")
    return pacotes_enviados

print("=============================================================================")
print("Inicio da execução: programa que calcula métricas UDP lado servidor")
print("Vinícius Yuji Hara e Eduardo Gabriel Kenzo Tanaka - Diciplina Redes de Computadores 2")
print("=============================================================================")

if len(sys.argv) < 2:
    print("Número de argumentos errados")
    sys.exit(1)
host = sys.argv[1]                                # Host do servidor
server_port = int(sys.argv[2])                    # Porta do servidor        

run_server(host, server_port)
