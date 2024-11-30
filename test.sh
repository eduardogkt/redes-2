#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ] || [ -z "$5" ] || [ -z "$6" ];
then
    echo "uso: ./test.sh <metrica> <tam_pacote> <nome_arquivo> <num_bytes> <host> <port>"
    exit 1;
fi

metrica=$1
tam_pacote=$2
nome_arquivo=$3
num_bytes=$4
host=$5
port=$6

echo "Entrada $metrica $tam_pacote $nome_arquivo $num_bytes $host $port"

n_tests=1

server_tcp=server_tcp.py
client_tcp=cliente_tcp.py

server_udp=server_udp.py
client_udp=cliente_udp.py

echo "Testes TCP"

server=$server_tcp
client=$client_tcp

port=8000

for run in $(seq 1 $n_tests);
do
    xterm -e "python3 $server $host $port; bash" &
    # gnome-terminal -- bash -c "python3 $server $host $port"

    sleep 1

    xterm -e "python3 $client $metrica $tam_pacote $nome_arquivo $num_bytes $host $port; bash" &
    # gnome-terminal -- bash -c "python3 $client $metrica $tam_pacote $nome_arquivo $num_bytes $host $port"
    
    port=$((port + 1))
done
