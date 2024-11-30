# Comparação entre protocolos TCP e UDP

Redes de Computadores II  
Universidade Federal do Paraná  
Departamento de Informática  
Bacharelado em Ciência da Computação

Eduardo Gabriel Kenzo Tanaka - GRR20211791  
Vinícius Yuji Hara - GRR20211763

### Descrição

Este trabalho tem como objetivo comparar o desempenho dos protocolos TCP e UDP. Para isso, foram consideradas as metricas de tempo, vazão e perda de dados na transferencia de arquivos e transferencia em memória principal entre servidor e cliente.  
Os programas de teste foram implementados em python utilizando as bibliotecas:  
**socket** para comunicação entre as máquinas;  
**time** para contagem de tempo;

### Projeto

#### Definição de métricas e casos de comparação

Serão consideradas as métricas tempo, vazão e quantidade de pacotes perdidos, para os seguintes casos de envio de dados: com/sem fragmentação e com/sem checksum.

#### Executando o trabalho

Para executar o trabalho com conexão TCP são utilzados os arquivos cliente_tcp.py e server_tcp.py. Para a conexão UDP são utilizados os arquivos cliente_udp.py e server_udp.py.

O server pode ser executado como exemplo abaixo:

```
python3 server_udp.py <host>
```

Em que:  
'host' é o nome da máquina do server

E o cliente pode ser executado:

```
python3 cliente_udp.py <metrica> <tam_pacote> <nome_arquivo> <num_bytes> <host> <port>
```

Em que:  
'métrica' pode ser "arquivo" para transferência de arquivo ou "memoria" para transferir em memória principal.
'tam_pacote' é o tamanho em bytes que o server vai mandar em cada pacote.
'nome_arquivo' é o arquivo que o cliente deseja obter do server ou escrever em seu diretório
'num_bytes' é o tamanho de bytes a ser transferido em memória, para arquivos usa-se 0.
'host' é o nome da máquina do server

Exemplo para server executando na máquina i29, porta 8000 do dinf
Server:

```
python3 server_udp.py i29
```

Cliente para tranferência de arquivo:

```
python3 cliente_udp.py arquivo 1024 exemplo.txt 0 i29 8000
```

Cliente para tranferência de dados em memória:

```
python3 cliente_udp.py memoria 1024 exemplo.txt 100000 i29 8000
```

### Conclusões