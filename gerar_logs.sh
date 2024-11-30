#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ] || [ -z "$5" ];
then
    echo "uso: ./test.sh <metrica> <nome_arquivo> <num_bytes> <host> <port>"
    exit 1;
fi

metrica=$1
nome_arquivo=$2
num_bytes=$3
host=$4
port=$5

server_tcp=server_tcp.py
client_tcp=client_tcp.py

server_udp=server_udp.py
client_udp=client_udp.py

log_dir=log_$metrica

mkdir -p server/$log_dir
mkdir -p client/$log_dir

# TESTES UDP ########################################

n_tests=5
server=$server_udp
client=$client_udp
port=8000

echo "TESTES UDP"
echo "METRICA $metrica"

for tam_pacote in {20,100,1024,1500,5000,10000,64000};
do
    echo "PACOTE TAM $tam_pacote"
    log="$log_dir/${tam_pacote}_udp.log"

    for run in $(seq 1 $n_tests);
    do
        echo "LOG CLIENT UDP" > client/$log
        echo "LOG SERVER UDP" > server/$log

        xfce4-terminal --working-directory="/home/eduardo/Faculdade/2024.2/redes2/server" \
                       --command="bash -c 'python3 $server $host $port >> $log'" 

        sleep 2

        xfce4-terminal --working-directory="/home/eduardo/Faculdade/2024.2/redes2/client" \
                       --command="bash -c 'python3 $client $metrica $tam_pacote $nome_arquivo $num_bytes $host $port >> $log'"

        port=$((port + 1))
    done
done


# TESTES TCP ########################################

n_tests=5
server=$server_tcp
client=$client_tcp
port=8000

echo "TESTES TCP"
echo "METRICA $metrica"

for tam_pacote in {20,100,1024,1500,5000,10000,64000};
do
    echo "PACOTE TAM $tam_pacote"
    log="$log_dir/${tam_pacote}_tcp.log"

    for run in $(seq 1 $n_tests);
    do
        echo "LOG CLIENT TCP" > client/$log
        echo "LOG SERVER TCP" > server/$log

        xfce4-terminal --working-directory="/home/eduardo/Faculdade/2024.2/redes2/server" \
                       --command="bash -c 'python3 $server $host $port >> $log'" 

        sleep 2

        xfce4-terminal --working-directory="/home/eduardo/Faculdade/2024.2/redes2/client" \
                       --command="bash -c 'python3 $client $metrica $tam_pacote $nome_arquivo $num_bytes $host $port >> $log'"

        port=$((port + 1))
    done
done
